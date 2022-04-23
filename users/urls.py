from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('users/login/', views.UsersLogin.as_view(), name='users_login'),
    path('users/passrecovery/', views.PassRecovery.as_view(),
         name='users_passrecovery'),
    path('users/passreset/<str:email>/<str:link>', views.NewPassWord.as_view(),
         name='users_passreset'),
    path('users/logout/', views.UserLogout.as_view(), name='users_logout'),
    path('users/register/',
         views.UserRegister.as_view(), name='users_register'),
    path('users/dashboard/', views.UserDashboard.as_view(),
         name='users_dashboard'),
    path('users/dashboard/delimovel', views.DeleteImovel.as_view(),
         name='users_delete_imovel'),
    path('users/dashboard/useredit', views.UserEdit.as_view(),
         name='users_edit'),
    path('users/dashboard/loginedit', views.LoginEdit.as_view(),
         name='login_edit'),
    path('users/dashboard/imoveis', views.DashBoardImoveis.as_view(),
         name='dashboard_imoveis'),
    path('users/dashboard/dadospessoais',
         views.DashBoardDadosPessoais.as_view(),
         name='dashboard_dadospessoais'
         ),
    path('users/dashboard/dadoslogin',
         views.DashBoardDadosLogin.as_view(),
         name='dashboard_dadoslogin'
         ),
    path('users/dashboard/mensagens',
         views.DashBoardMensagens.as_view(),
         name='dashboard_mensagens'
         ),

    path('users/dashboard/mensagens/<int:idmsg>',
         views.DashBoardMensagens.as_view(),
         name='dashboard_mensagem'
         ),

]
