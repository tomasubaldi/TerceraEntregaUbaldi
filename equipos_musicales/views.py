from django.shortcuts import render, get_object_or_404
from .models import EquipoMusical

def lista_equipos_musicales(request):
    equipos = EquipoMusical.objects.all()
    return render(request, 'lista_equipos_musicales.html', {'equipos': equipos})

def buscar_equipo_musical(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        equipos = EquipoMusical.objects.filter(descripcion__icontains=query)
        return render(request, 'buscar_equipo_musical.html', {'equipos': equipos})
    else:
        return render(request, 'buscar_equipo_musical.html')