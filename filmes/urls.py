from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrarFilme/', views.cadastrarFilme, name='cadastrarFilme'),
]
