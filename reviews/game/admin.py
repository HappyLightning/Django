from django.contrib import admin
from game.models import Jogo, Genero

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Jogo._meta.fields]
    list_filter = ['titulo', 'genero', 'desenvolvedor', 'nota', 'data_lançamento']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']
