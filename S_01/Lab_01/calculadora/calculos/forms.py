from django import forms

class CalculadoraForm(forms.Form):
    numero1 = forms.FloatField(label="Número 1")
    numero2 = forms.FloatField(label="Número 2")
    OPERACIONES = [
        ('suma', 'Suma'),
        ('resta', 'Resta'),
        ('multiplicacion', 'Multiplicación'),
        ('division', 'División'),
    ]
    operacion = forms.ChoiceField(choices=OPERACIONES, label="Operación")
