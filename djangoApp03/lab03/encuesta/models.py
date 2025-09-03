from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicación')

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)