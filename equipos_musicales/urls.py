from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.buscar_equipo_musical, name='buscar_equipo_musical'),
    path('crear-equipo-musical/', views.crear_equipo_musical, name='crear_equipo_musical'),
    path('lista/', views.lista_equipos_musicales, name='lista_equipos_musicales'),
    ]
