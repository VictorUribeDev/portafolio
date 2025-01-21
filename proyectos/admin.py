from django.contrib import admin
from django.utils.html import format_html
from .models import Proyecto

    

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'link_clickable', 'iconos_preview')
    fields = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'link', 'imagen', 'iconos')

    def link_clickable(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank">Abrir proyecto</a>', obj.link)
        return "No disponible"
    link_clickable.short_description = 'Link del proyecto'

    def iconos_preview(self, obj):
        if isinstance(obj.iconos, str):
            iconos_html = ''.join(
                f'<i class="{icono.strip()}" style="font-size: 24px; margin-right: 8px; color: #6c757d;"></i>'
                for icono in obj.iconos.split(',')
            )
            return format_html(iconos_html)
        return "No asignado"
    iconos_preview.short_description = 'Iconos'


   


    class Meta:
        model = Proyecto
        fields = '__all__'