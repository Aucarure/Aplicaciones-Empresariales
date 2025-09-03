from django.shortcuts import render
from .models import Cliente, Producto, Venta

def index(request):
    return render(request, 'ventas_app/index.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas_app/clientes.html', {'clientes': clientes})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas_app/productos.html', {'productos': productos})

def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas_app/ventas.html', {'ventas': ventas})
