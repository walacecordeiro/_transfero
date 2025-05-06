from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm

# Create your views here.

def login(request):
    return render(
        request,
        'login.html',
    )
    
def criarUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('/usuarios/login')
        
    else:
        form = UsuarioForm()
        
    return render(
        request,
        'cadastro.html',
        {'form': form}
    )