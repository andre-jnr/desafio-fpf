# Generated by Django 5.2 on 2025-04-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.FloatField()),
                ('num2', models.FloatField()),
                ('num3', models.FloatField()),
                ('status', models.CharField(choices=[('processando', 'Processando'), ('concluido', 'Concluído')], default='processando', max_length=20)),
                ('media', models.FloatField(blank=True, null=True)),
                ('mediana', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
