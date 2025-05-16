from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastrar/', views.criarUsuario, name='cadastrarUsuario'),
    path('login/', views.login, name='loginUsuario'),
]
