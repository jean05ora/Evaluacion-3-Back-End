from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala
from .forms import ReservaForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {}

    salas = Sala.objects.all()

    context['salas'] = salas

    return render(request, 'index.html', context)

def tipos_sala(request):
    salas = Sala.objects.all()
    
    tipos = {}
    for s in salas:
        if s.tipo_sala not in tipos:
            tipos[s.tipo_sala] = s.capacidad
        else:
            if s.capacidad > tipos[s.tipo_sala]:
                tipos[s.tipo_sala] = s.capacidad

    return render(request, 'tipos_sala.html', {'tipos': tipos})


def salas_tipo(request, tipo):
    salas = Sala.objects.filter(tipo_sala=tipo)

    return render(request, 'salas.html', {'salas':salas, 'tipo':tipo})




def reserva(request, pk):
    sala = Sala.objects.get(pk=pk)
    if not sala.disponible():
        return redirect("salas_tipo", tipo=sala.tipo_sala)

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.sala = sala
            reserva.save()
            return redirect("salas_tipo", tipo=sala.tipo_sala)
    else:
        form = ReservaForm()

    return redirect("salas_tipo", tipo=sala.tipo_sala)
