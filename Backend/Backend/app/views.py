from django.shortcuts import render
from .forms import ContactoForm

def home(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'app/home.html', data)

def terminos(request):
    return render(request, 'app/terminos.html')

def olvidada(request):
    return render(request, 'app/olvidada.html')
