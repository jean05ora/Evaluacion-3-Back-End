from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reserva<int:pk>/", views.reserva, name="reservar"),
    path("salas/", views.tipos_sala, name="tipos_sala"),
    path("salas/<str:tipo>", views.salas_tipo, name="salas_tipo"),
]