from django.shortcuts import redirect,render

from filmes.forms import FilmeForm
from sistema.models import Filme

# Create your views here.


def listarFilmes(request):
    filmes = Filme.objects.all()
    
    context = {
        'filmes' : filmes
    }
    
    return render(
        request,
        'filmes/listar.html',
        context
    )

def cadastrarFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar-filmes')
        
    else:
        form = FilmeForm()
    
    return render(
        request,
        'filmes/cadastro.html',
        {'form': form}
    )