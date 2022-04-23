
from django.db import models
from imoveis.models import Imovel
from users.models import User

# Create your models here.


class Chat(models.Model):

    titulo = models.CharField(max_length=65, default='Vamos fechar negócio?')
    locador = models.ForeignKey(User, on_delete=models.CASCADE)
    propietario = models.IntegerField(default=0)
    imovel_id = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.titulo


class Mensagens(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    autor = models.IntegerField(default=0)
    destinatario = models.IntegerField(default=0)
    mensagem = models.TextField(default='')
    data = models.DateTimeField(auto_now_add=True, blank=True)
    lida = models.CharField(max_length=3, default='nao')

    class Meta:
        default_related_name = 'chatmensagens'

    def __str__(self):
        return self.mensagem
