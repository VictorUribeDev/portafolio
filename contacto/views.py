from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MensajeForm

def contacto_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
            return redirect('home')  
    else:
        form = MensajeForm()

    return render(request, 'contacto.html', {'form': form})