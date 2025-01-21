from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True) 
    iconos = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="'fa-brands fa-html5, fa-brands fa-bootstrap, fa-brands fa-js, fa-brands fa-python, fa-solid fa-database, fa-solid fa-gamepad'"
        )
    
    
