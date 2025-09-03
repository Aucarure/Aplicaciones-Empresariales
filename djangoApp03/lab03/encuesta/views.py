from django.shortcuts import render, get_object_or_404
from .models import Pregunta, Opcion

def index(request):
    latest_question_list = Pregunta.objects.order_by('-fecha_pub')[:5]  # 👈 usamos fecha_pub
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'encuesta/index.html', context)

def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    context = {
        'pregunta': pregunta
    }
    return render(request, 'encuesta/detalle.html', context)

def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    opcionSeleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    opcionSeleccionada.votos += 1
    opcionSeleccionada.save()
    context = {
        'pregunta': pregunta
    }
    return render(request, 'encuesta/resultados.html', context)
