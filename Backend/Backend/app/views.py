from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def terminos(request):
    return render(request, 'app/terminos.html')

def olvidada(request):
    return render(request, 'app/olvidada.html')

