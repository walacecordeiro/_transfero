from django.contrib import admin

from sistema import models

# Registrar os models aqui.

# Aqui fica o registro do Usuário.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)
 
# Aqui fica o registro do Filme
@admin.register(models.Filme)
class FilmesAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'estudio', 'genero',)

# Aqui fica o registro do Gênero
@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'data_cadastro',)