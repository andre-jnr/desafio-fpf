from django.urls import path
from .views import ProcessarAPIView, StatusAPIView

urlpatterns = [
    path('processar/', ProcessarAPIView.as_view(), name='processar'),
    path('status/<int:pk>/', StatusAPIView.as_view(), name='status'),
]
