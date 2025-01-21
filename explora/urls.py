from django.urls import path
from . import views

urlpatterns = [
    path('', views.explora_view, name='explora'),  # Ruta principal para la app 'proyectos'
]
