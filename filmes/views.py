from django.shortcuts import redirect,render

from filmes.forms import FilmeForm

# Create your views here.

def cadastrarFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/listar-filmes')
        
    else:
        form = FilmeForm()
    
    return render(
        request,
        'filmes/cadastro.html',
        {'form': form}
    )