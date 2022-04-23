# url_replace.py
# https://www.dicas-de-django.com.br/38-django-paginacao-filtros
# Referência acima

from django import template

register = template.Library()

# Função para utilizar GET + Paginação


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.pop('page', None)
    query.update(kwargs)
    return query.urlencode()
