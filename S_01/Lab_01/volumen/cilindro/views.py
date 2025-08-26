from django.shortcuts import render
import math

def calcular_cilindro(request):
    if request.method == "POST":
        try:
            radio = float(request.POST.get("radio", 0))
            altura = float(request.POST.get("altura", 0))
            volumen = math.pi * (radio ** 2) * altura
            return render(request, "cilindro/resultado_cilindro.html", {
                "radio": radio,
                "altura": altura,
                "volumen": volumen
            })
        except ValueError:
            return render(request, "cilindro/resultado_cilindro.html", {
                "error": "Por favor ingresa valores numéricos válidos."
            })

    return render(request, "cilindro/cilindro.html")
