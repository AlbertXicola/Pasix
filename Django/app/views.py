from django.shortcuts import render, redirect
# from .models import Producto
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
import os
from .pycore import *
from django.http import JsonResponse
import pymongo
from bson.objectid import ObjectId
from .models import Fichero
import datetime



def cierre(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'app/home.html')

def pycore_view(request):
    return render(request, 'registration/pycore.html')

def test(request):
    return render(request, 'registration/test.html')

def galeria(request):
    return render(request, 'app/galeria.html')

def olvidada(request):
    return render(request, 'app/olvidada.html')

def terminos(request):
    return render(request, 'app/terminos.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def archivos(request):
    ficheros = Fichero.objects.filter(id_usuario = request.user.id)  # Ejemplo: selecciona el primer objeto de la tabla Fichero
    return render(request, 'app/archivos.html', {'ficheros': ficheros})



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





@csrf_exempt
@login_required



def analisis(request):
    if request.method == 'POST':
        archivos = request.FILES.getlist('files[]')

        if not archivos:
            return render(request, 'registration/pycore.html', {'message_select': 'Archivo Erroneo o No se ha seleccionado Archivo'})

        if not os.path.exists(carpeta_Para_analizar):  # Asegurarse de que el directorio para analizar exista
            os.makedirs(carpeta_Para_analizar)

        resultados = []  # Lista para almacenar resultados de los archivos subidos

        for archivo in archivos:
            archivo_path = os.path.abspath(os.path.join(carpeta_Para_analizar, archivo.name))
            # print("Ruta del archivo:", archivo_path)  # Agregar esta línea para imprimir la ruta del archivo
            with open(archivo_path, 'wb') as destination:
                for chunk in archivo.chunks():
                    destination.write(chunk)

            resultado_procesamiento = procesar_archivo(archivo_path)  # Procesar el archivo y obtener el resultado específico
            # print("Resultado del procesamiento:", resultado_procesamiento)  # Agregar esta línea para imprimir el resultado del procesamiento
            resultados.append(resultado_procesamiento)  # Agregar el resultado a la lista de resultados

            # Autenticación en MongoDB
            client = MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
            db = client["Proyecto"]
            collection = db["Archivos"]

            # Buscar el documento asociado al nombre del archivo
            documento = collection.find_one({"Nombre_Archivo": archivo.name})
            if documento:
                id_archivo = documento["_id"]
                #print (id_archivo)
            
            if request.user.is_authenticated:
                id_usuario = request.user.id
            
            fichero = Fichero(id_archivo=id_archivo, id_usuario=id_usuario)
            fichero.save()

        

        return render(request, 'app/analisis.html', {'message': 'Carga exitosa', 'resultados': resultados})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

    



def archivos(request):


    client = MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
    db = client["Proyecto"]
    collection = db["Archivos"]


    id_usuario_actual = request.user.id
    django_data = Fichero.objects.filter(id_usuario=id_usuario_actual)



    now = "dater"
    nombre_usuario = request.user.username
    id_usuario = request.user.id


    #print("=======================================")
    #print(f"Archivos del usuario @{nombre_usuario} con ID = {id_usuario}:")
    #print("=======================================")

    archivos_data = []
    for fichero in django_data:
        ficheros_mongo = collection.find({"_id": ObjectId(fichero.id_archivo)})
        for fichero_mongo in ficheros_mongo:
            nombre_archivo = fichero_mongo.get('Nombre_Archivo')
            Anomalias = fichero_mongo.get('Maldades')
            Estado = fichero_mongo.get('Prevision')
            archivos_data.append({
                'nombre_archivo': nombre_archivo,
                'anomalias': Anomalias,
                'prevision': Estado,
            })

    now = datetime.datetime.now()  

    context = {
        'archivos_data': archivos_data,
        'now': now,
        'nombre_usuario': nombre_usuario,
        'id_usuario': id_usuario
    }

    return render(request, 'app/archivos.html', context)