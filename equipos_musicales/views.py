from django.shortcuts import render, redirect,  get_object_or_404
from .models import EquipoMusical
from equipos_musicales.forms import EquipoMusicalForm
from .forms import EquipoMusicalForm



def home(request):
     return render(request, 'equipos_musicales/home.html' )


def crear_equipo_musical(request):
    if request.method == 'POST':
        form = EquipoMusicalForm(request.POST)
        if form.is_valid():
            equipo_musical = EquipoMusical()
            equipo_musical.marca = form.cleaned_data['marca']
            equipo_musical.modelo = form.cleaned_data['modelo']
            equipo_musical.potencia = form.cleaned_data['potencia']
            equipo_musical.descripcion = form.cleaned_data['descripcion']
            equipo_musical.save()
            return redirect('lista_equipos_musicales')
    else:
        form = EquipoMusicalForm()
    return render(request, 'equipos_musicales/home.html', {'form': form})


def lista_equipos_musicales(request):
    equipos = EquipoMusical.objects.all()
    return render(request, 'equipos_musicales/lista_equipos_musicales.html', {'equipos': equipos})

def buscar_equipo_musical(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        equipos = EquipoMusical.objects.filter(descripcion__icontains=query)
        return render(request, 'equipos_musicales/buscar_equipo_musical.html', {'equipos': equipos})
    else:
        return render(request, 'equipos_musicales/buscar_equipo_musical.html')

