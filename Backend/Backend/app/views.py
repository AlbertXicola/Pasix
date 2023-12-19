from django.shortcuts import render, redirect
from .forms import ContactoForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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

# En tu archivo views.py


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nombre_de_la_vista_o_url')  # Reemplaza con la URL correcta
    else:
        form = UserCreationForm()

    return render(request, 'app/usuario.html', {'form': form})