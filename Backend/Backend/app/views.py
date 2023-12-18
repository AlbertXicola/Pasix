from django.shortcuts import render

from .forms import ContactoForm, ProductoForms

def home(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'app/home.html', data)

def terminos(request):
    return render(request, 'app/terminos.html')

def olvidada(request):
    return render(request, 'app/olvidada.html')


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="contacto guardado"
        else:
            data["form"] = formulario
            data["mensaje"] ="error"

    return render(request, 'app/contacto.html', data)

def agregar_producto(request):


    data = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario


    return render(request, 'app/producto/agregar.html', data)
