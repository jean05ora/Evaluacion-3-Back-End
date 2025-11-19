from django.db import models
from django.utils import timezone

# Create your models here.
class Sala(models.Model):
    nombre_sala = models.CharField(max_length=155)
    numero_sala = models.PositiveIntegerField(null=True, blank=True)
    tipo_sala = models.CharField(max_length=55, null=True, blank=True)
    capacidad = models.PositiveIntegerField()
    
    def disponible(self):
        now = timezone.now()
        reserva = self.reserva_set.filter(fecha_inicio__lte = now, fecha_fin__gt = now).first()
        return reserva is None

    def __str__(self):
        return self.nombre_sala
    
class Reserva(models.Model):
    rut = models.CharField(max_length=12)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sala.nombre_sala