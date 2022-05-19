from django.contrib.auth.models import User

from celery import shared_task


@shared_task
def add_user(username, password):
    User.objects.get_or_create(username=username, password=password)
