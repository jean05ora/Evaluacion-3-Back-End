from django import forms 
from .models import Sala, Reserva
from datetime import timedelta
from django.utils import timezone

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut']

    def save(self, commit=True):
        reserva = super().save(commit=False)
        reserva.fecha_inicio = timezone.now()
        reserva.fecha_fin = reserva.fecha_inicio + timedelta(hours = 2)

        if commit:
            reserva.save()
        return reserva