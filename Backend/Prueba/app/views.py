from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreatrionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)


# Create your views here.
# @permission_required('app.add_galeria')EJEMPLoooooooooooooooooooooooo
def galeria(request):
    return render(request, 'app/galeria.html')
# Create your views here.

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario



    return render(request, 'app/contacto.html', data)
# Create your views here.


def registro(request):
    data= {
        'form':CustomUserCreatrionForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreatrionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "registro correcto")
            return redirect(to="home")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)