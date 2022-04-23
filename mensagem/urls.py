from django.urls import path

from . import views

app_name = 'mensagem'

urlpatterns = [
    path('msg/send', views.ChatMessages.as_view(), name='send_msg'),
    path('email/contato', views.Contato.as_view(), name='email_contato')
]
