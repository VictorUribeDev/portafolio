# proyectos/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split_icons(value):
    if isinstance(value, str):
        # Dividimos la cadena por comas y eliminamos los espacios extra de cada icono
        return [icono.strip() for icono in value.split(',')]
    return []
