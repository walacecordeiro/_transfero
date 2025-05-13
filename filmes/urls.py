from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.cadastrarFilme, name='cadastrar'),
    path('listar/', views.listarFilmes, name='listar'),
]
