from django.shortcuts import render, get_object_or_404
from .models import Autor, Entrada

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, "blog/lista_autores.html", {"autores": autores})

def entrada_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    entradas = Entrada.objects.filter(autor=autor)
    return render(request, "blog/entradas_por_autor.html", {"autor": autor, "entradas": entradas})
