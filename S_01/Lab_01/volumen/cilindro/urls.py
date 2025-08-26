from django.urls import path
from . import views

urlpatterns = [
    path('cilindro/', views.calcular_cilindro, name='cilindro'),
]
