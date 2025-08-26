from django.shortcuts import render, redirect
from .forms import CalculadoraForm

def formulario_view(request):
    if request.method == "POST":
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['numero1']
            n2 = form.cleaned_data['numero2']
            operacion = form.cleaned_data['operacion']
            return redirect('resultado', n1=n1, n2=n2, operacion=operacion)
    else:
        form = CalculadoraForm()
    return render(request, "calculos/formulario.html", {"form": form})


def resultado_view(request, n1, n2, operacion):
    n1 = float(n1)
    n2 = float(n2)
    resultado = None

    if operacion == 'suma':
        resultado = n1 + n2
    elif operacion == 'resta':
        resultado = n1 - n2
    elif operacion == 'multiplicacion':
        resultado = n1 * n2
    elif operacion == 'division':
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "Error: División entre cero"

    return render(request, "calculos/resultado.html", {
        "n1": n1,
        "n2": n2,
        "operacion": operacion,
        "resultado": resultado
    })
