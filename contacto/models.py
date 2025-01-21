from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-fecha_envio']


class DestinatarioContacto(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email