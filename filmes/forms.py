from django import forms
from sistema.models import Filme, Genero

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano_lancamento', 'estudio', 'genero', 'sinopse']