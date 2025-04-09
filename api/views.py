from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Processamento
from .serializers import ProcessamentoSerializer
from .tasks import processar_numeros

class ProcessarAPIView(APIView):
    def post(self, request):
        serializer = ProcessamentoSerializer(data=request.data)
        if serializer.is_valid():
            processamento = serializer.save()
            processar_numeros.delay(processamento.id)
            return Response({"id": processamento.id, "status": processamento.status}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusAPIView(APIView):
    def get(self, request, pk):
        try:
            processamento = Processamento.objects.get(pk=pk)
            return Response(ProcessamentoSerializer(processamento).data)
        except Processamento.DoesNotExist:
            return Response({"error": "Registro não encontrado"}, status=status.HTTP_404_NOT_FOUND)