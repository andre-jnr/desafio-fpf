from celery import shared_task
from .models import Processamento

def calcular_mediana(valores):
    valores.sort()
    return valores[1]

@shared_task
def processar_numeros(processamento_id):
    processamento = Processamento.objects.get(id=processamento_id)
    numeros = [processamento.num1, processamento.num2, processamento.num3]
    processamento.media = sum(numeros) / 3
    processamento.mediana = calcular_mediana(numeros)
    processamento.status = "concluido"
    processamento.save()
