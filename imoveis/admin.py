
from django.contrib import admin

from .models import Imovel, ImovelFoto


class ImovelFotoAdmin(admin.StackedInline):
    model = ImovelFoto


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImovelFotoAdmin]

    list_display = [
        'id',
        'titulo',
    ]
    list_display_links = list_display
