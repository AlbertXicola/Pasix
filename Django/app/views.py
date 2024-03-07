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
    return render(request, 'registration/pycore.html')

def test(request):
    return render(request, 'registration/test.html')


from .pycore import *
from django.http import JsonResponse



@csrf_exempt
@login_required
def analisis(request):
    if request.method == 'POST':
        archivos = request.FILES.getlist('files[]')

        if not archivos:
            return render(request, 'registration/pycore.html', {'message_select': 'Archivo Erroneo o No se ha selccionado Archivo'})


        # Asegurarse de que el directorio para analizar exista
        if not os.path.exists(carpeta_Para_analizar):
            os.makedirs(carpeta_Para_analizar)

        resultados = []  # Lista para almacenar resultados de los archivos subidos

        for archivo in archivos:
            archivo_path = os.path.abspath(os.path.join(carpeta_Para_analizar, archivo.name))
            print("Ruta del archivo:", archivo_path)  # Agregar esta línea para imprimir la ruta del archivo
            with open(archivo_path, 'wb') as destination:
                for chunk in archivo.chunks():
                    destination.write(chunk)

            # Procesar el archivo y obtener el resultado específico
            resultado_procesamiento = procesar_archivo(archivo_path)
            print("Resultado del procesamiento:", resultado_procesamiento)  # Agregar esta línea para imprimir el resultado del procesamiento

            # Agregar el resultado a la lista de resultados
            resultados.append(resultado_procesamiento)

        print(resultados)

        # Puedes devolver una respuesta JSON con los resultados de los archivos subidos
        return render(request, 'app/analisis.html', {'message': 'Carga exitosa', 'resultados': resultados})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def archivos(request):
    return render(request, 'app/archivos.html')
