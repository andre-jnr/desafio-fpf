from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio_fpf.settings")

app = Celery("desafio_fpf")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
