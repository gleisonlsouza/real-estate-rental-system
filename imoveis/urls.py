from django.urls import path

from . import views

app_name = 'imoveis'

urlpatterns = [
    path(
        'imoveis/',
        views.ImoveisViewList.as_view(),
        name='imoveis_view_list'
    ),

    path(
        'imoveis/detail/<int:pk>',
        views.ImoveisViewDetail.as_view(),
        name='imoveis_view_detail'
    ),

    path(
        'imoveis/new/',
        views.ImoveisAddEdit.as_view(),
        name='imoveis_new'
    ),

    path(
        'imoveis/<int:pk>/edit/',
        views.ImoveisAddEdit.as_view(),
        name='imoveis_edit'
    ),

    path(
        'imoveis/<int:imovelID>/foto/<int:fotoID>/delete/',
        views.ImovelFotoDelete.as_view(),
        name='imoveis_foto_delete'
    ),

    path(
        'imoveis/<int:imovelID>/fotoupload/',
        views.ImovelFotoUpload.as_view(),
        name='imoveis_foto_upload'
    ),
]
