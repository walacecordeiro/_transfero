from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrarFilme/', views.cadastrarFilme, name='cadastrarFilme'),
    path('listar-filmes/', views.listarFilmes, name='listar-filmes'),
]
