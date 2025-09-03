from django.urls import path
from . import views

app_name = 'ventas_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('ventas/', views.ventas, name='ventas'),
]
