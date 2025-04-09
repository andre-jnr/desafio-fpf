from django.db import models


class Processamento(models.Model):
    STATUS_CHOICES = [
        ("processando", "Processando"),
        ("concluido", "Concluído")
    ]
    num1 = models.FloatField()
    num2 = models.FloatField()
    num3 = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="processando")
    media = models.FloatField(null=True, blank=True)
    mediana = models.FloatField(null=True, blank=True)