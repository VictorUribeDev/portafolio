from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos_view, name='proyectos'),  # Ruta principal para la app 'proyectos'
]
