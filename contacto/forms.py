from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'asunto', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tu correo electrónico'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'El asunto de tu mensaje'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tu número de teléfono (opcional)'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Escribe tu mensaje aquí',
                'rows': 5
            }),
        }
