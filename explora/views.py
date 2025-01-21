from django.shortcuts import render

# Create your views here.
def explora_view(request):
    return render(request, 'explora.html')