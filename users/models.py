from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    choices_locador_proprietario = (
        ('locador', 'Locador'),
        ('proprietario', 'Proprietário')
    )

    celular = models.CharField(max_length=20, blank=True)
    tipo_usuario = models.CharField(
        max_length=12, choices=choices_locador_proprietario, default='locador')


class PasswordReset(models.Model):

    email = models.CharField(max_length=200)
    user_id = models.IntegerField()
    ip = models.CharField(max_length=15)
    link = models.CharField(max_length=250)
    recuperado = models.CharField(max_length=3, default='nao')
    data_pedido = models.DateTimeField(auto_now_add=True)
    validade = models.DateTimeField(default=timezone.now()+timedelta(days=3))

    def __str__(self):
        return self.email
