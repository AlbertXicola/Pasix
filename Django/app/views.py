from django.shortcuts import render, redirect
# from .models import Producto
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
import os



def home(request):
    return render(request, 'app/home.html')

def archivos(request):
    return render(request, 'app/archivos.html')
    

def cierre(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige a la página de inicio (asumiendo que 'home' es el nombre de la URL para la página de inicio)

# Create your views here.
# @permission_required('app.add_galeria')EJEMPLoooooooooooooooooooooooo
def galeria(request):
    return render(request, 'app/galeria.html')

# Create your views here.

def olvidada(request):
    return render(request, 'app/olvidada.html')

def terminos(request):
    return render(request, 'app/terminos.html')


def perfil(request):
    return render(request, 'app/perfil.html')


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado correctamente"
        else:
            data["form"] = formulario



    return render(request, 'app/contacto.html', data)
# Create your views here.


def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()  # Guarda al usuario directamente
            login(request, user)
            messages.success(request, "Registro correcto")
            return redirect('home')

    return render(request, 'registration/registro.html', data)


def user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión después del registro
            return redirect('user')  # Redirige a la página deseada después del registro
    else:
        form = UserCreationForm()

    return render(request, 'app/user.html', {'form': form})




def pycore_view(request):
    return render(request, 'pycore.html')

def test(request):
    return render(request, 'test.html')


