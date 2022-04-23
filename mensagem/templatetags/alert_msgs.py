from django import template
from mensagem.models import Mensagens

register = template.Library()


@register.simple_tag
def alert_msgs(request):
    qtd_msgs = Mensagens.objects.filter(
        destinatario=request.user.id,
        lida='nao',
    )

    return qtd_msgs.count()


@register.simple_tag
def unread_qtd_msgs(request, chat_id):
    qtd_msgs = Mensagens.objects.filter(
        destinatario=request.user.id,
        chat_id=chat_id,
        lida='nao',
    )

    return qtd_msgs.count()
