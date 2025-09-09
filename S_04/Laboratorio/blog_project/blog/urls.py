from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_autores, name="lista_autores"),
    path("autor/<int:autor_id>/", views.entrada_por_autor, name="entradas_por_autor"),
]
