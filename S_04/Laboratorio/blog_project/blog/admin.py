from django.contrib import admin
from .models import Autor, Entrada


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor") 
    list_filter = ("autor",)
    search_fields = ("titulo", "contenido")
