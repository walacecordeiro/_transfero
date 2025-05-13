from django.shortcuts import render
from sistema.models import Usuario


def listaUsuarios(request):
    usuarios = Usuario.objects.all()
    
    context = {
        'usuarios' : usuarios
    }
    
    return render(
        request,
        'sistema/listar.html',
        context,
    )