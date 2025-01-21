from django.shortcuts import render
from .models import Proyecto  # Asegúrate de tener un modelo llamado Proyecto

def proyectos_view(request):
    proyectos = Proyecto.objects.all()  # Obtiene todos los proyectos de la base de datos
    return render(request, 'proyectos.html', {'proyectos': proyectos})
