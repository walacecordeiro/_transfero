from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastrar/', views.criarUsuario, name='cadastrar'),
    path('login/', views.login, name='login'),
]
