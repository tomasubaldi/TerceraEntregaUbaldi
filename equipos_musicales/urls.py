from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_elemento, name='crear_elemento'),
    path('buscar/', views.buscar_elemento, name='buscar_elemento'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
]
