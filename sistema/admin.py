from django.contrib import admin

from sistema import models

# Registrar os models aqui.

# Aqui fica o registro do Usuário.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)