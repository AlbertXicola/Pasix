from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
import os
from .pycore import *
from django.http import JsonResponse
import pymongo
from bson.objectid import ObjectId
from .models import Fichero
import datetime
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Compartido
from django.contrib.auth.decorators import login_required
from .models import Fichero
from bson import ObjectId
from .models import Fichero
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Compartido
from django.shortcuts import render
from .forms import ContactoForm
from django.shortcuts import get_object_or_404, redirect
from .models import Fichero, Compartido






def cierre(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'app/home.html')

def usuario(request):
    usuario = request.user
    data = {}  # Crear un diccionario para almacenar los datos a pasar a la plantilla
    data['form'] = ContactoForm(initial={'nombre': usuario.username, 'correo': usuario.email})

    return render(request, 'app/usuario.html', data)

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




def contacto(request):
    data = {}

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado correctamente"
            # Crear un nuevo formulario vacío
            data["form"] = ContactoForm()
        else:
            data["form"] = formulario
    else:
        if request.user.is_authenticated:
            usuario = request.user
            data['form'] = ContactoForm(initial={'nombre': usuario.username, 'correo': usuario.email})
        else:
            data['form'] = ContactoForm()

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
            return redirect('app/usuario.html')  # Redirige a la página deseada después del registro
    else:
        form = UserCreationForm()

    return render(request, 'app/usuario.html', {'form': form})





@csrf_exempt
@login_required
def analisis(request):
    if request.method == 'POST':
        archivos = request.FILES.getlist('files[]')

        if not archivos:
            return render(request, 'registration/pycore.html', {'message_select': 'No se ha seleccionado Archivo o Formato Erroneo'})

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
            
            fichero = Fichero(id_archivo=id_archivo, id_usuario=id_usuario, hora_analizado=timezone.now())

            fichero.save()

        

        return render(request, 'app/analisis.html', {'message': 'Carga exitosa', 'resultados': resultados})

    return JsonResponse({'error': 'Método no permitido'}, status=405)





def archivos(request):


    client = MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
    db = client["Proyecto"]
    collection = db["Archivos"]


    id_usuario_actual = request.user.id
    django_data = Fichero.objects.filter(id_usuario=id_usuario_actual)




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
            nuestrohash = fichero_mongo.get('Our_Hash')
            hashapi = fichero_mongo.get('id_API')
            hora_analizado = fichero.hora_analizado.strftime("%Y-%m-%d %H:%M:%S") if fichero.hora_analizado else "N/A"
            archivos_data.append({
                'nombre_archivo': nombre_archivo,
                'anomalias': Anomalias,
                'prevision': Estado,
                'hora_analizado': hora_analizado,  # Asegúrate de incluir la hora analizada en el diccionario de datos
                'id': fichero.id,
                'nuestrohash': nuestrohash,
                'hashapi': hashapi,
            })
    usuarios = User.objects.all()
    context = {
       'archivos_data': archivos_data,
       'nombre_usuario': nombre_usuario,
       'id_usuario': id_usuario,
       'ficheros': django_data,  # Añadir los ficheros completos al contexto
       'usuarios': usuarios   }

    return render(request, 'app/archivos.html', context)





def eliminar_fichero(request, fichero_id):
    # Obtener el objeto Fichero que se va a eliminar
    fichero = get_object_or_404(Fichero, id=fichero_id)
    
    # Eliminar el registro de compartidos asociados a este archivo
    Compartido.objects.filter(id_archivo=fichero_id).delete()
    
    # Eliminar el objeto Fichero
    fichero.delete()
    
    # Redireccionar a la página de archivos después de eliminar el registro
    return redirect('archivos')





def descargar_archivo(request, nombre_archivo):
    # Ruta del archivo

        # Definir la ruta base
   # ruta_base_Limpio = '/home/pasix/Descargas/Pasix/Finalizado/Limpio'
   # ruta_base_Cuarentena = '/home/pasix/Descargas/Pasix/Finalizado/Cuarentena'
   # ruta_base_Malicioso = '/home/pasix/Descargas/Pasix/Finalizado/Malicioso'

   # if anomalias == 0:
   #     ruta_archivo = os.path.join(ruta_base_Limpio, nombre_archivo)
   # elif 1 <= anomalias <= 5:
   #     ruta_archivo = os.path.join(ruta_base_Cuarentena, nombre_archivo)
   # elif 6 <= anomalias <= 1000:
   #     ruta_archivo = os.path.join(ruta_base_Malicioso, nombre_archivo)
    

    ruta_base = os.path.join('/home/pasix/Descargas/Pasix/Finalizado', nombre_archivo)  
    
    # Verificar si el archivo existe
    if os.path.exists(ruta_base):
        # Abrir el archivo y devolverlo como una respuesta de archivo
        with open(ruta_base, 'rb') as archivo:
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
            print("Ruta del archivo:", ruta_base)

            return response
    else:
        # Si el archivo no existe, devolver un error 404
        return HttpResponse(status=404)





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Compartido

def compartir_archivo(request):
    if request.method == 'POST':
        id_usuario = request.user.id  
        id_archivo = request.POST.get('id_fichero')
        usuarios_compartir = request.POST.getlist('usuarios_compartir[]')  # Obtener lista de usuarios seleccionados

        for id_usuariocompartido in usuarios_compartir:
            compartido = Compartido.objects.create(id_usuario=id_usuario, id_ucompartido=id_usuariocompartido, id_archivo=id_archivo)
            compartido.save()
        
        messages.success(request, 'Archivo compartido exitosamente')
        return redirect('archivos')  # Redirige a la vista 'archivos' definida en tus patrones de URL

    return redirect('app/archivos.html')


@login_required
def compartido(request):
    client = MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
    db = client["Proyecto"]
    collection = db["Archivos"]

    usuario_sesion = request.user.id
    
    archivos_compartidos = Compartido.objects.filter(id_ucompartido=usuario_sesion)
    
    archivos_con_documentos = []

    for archivo_compartido in archivos_compartidos:
        usuario_compartido = User.objects.get(id=archivo_compartido.id_usuario)
        archivo_compartido.nombre_usuario = usuario_compartido.username
        
        id_archivo_compartido = archivo_compartido.id_archivo
        
        fichero = None
        
        try:
            fichero = Fichero.objects.get(id=id_archivo_compartido)
        except Fichero.DoesNotExist:
            pass
        
        if fichero is not None:
            ficheros_mongo = collection.find({"_id": ObjectId(fichero.id_archivo)})
            hora_analizado = fichero.hora_analizado.strftime("%Y-%m-%d %H:%M:%S") if fichero.hora_analizado else "N/A"

            documentos_archivo = []
            for documento in ficheros_mongo:

                documentos_archivo.append({
                    'id_archivo': documento["_id"],
                    'nombre_archivo': documento["Nombre_Archivo"],
                    'Maldades': documento["Maldades"],
                    'Prevision': documento["Prevision"],
                    'hora_analizado': hora_analizado,
                    'nuestrohash': documento["Our_Hash"],
                    'hashapi': documento ["id_API"],
                })
                
            archivos_con_documentos.append({
                'archivo_compartido': archivo_compartido,
                'documentos': documentos_archivo
            })

    context = {
        'archivos_con_documentos': archivos_con_documentos,
        'Nombre_usuario_actual': request.user.username
    }

    return render(request, 'app/compartido.html', context)



def eliminar_fichero_compartido(request, id):
    compartido = get_object_or_404(Compartido, id=id)
    compartido.delete()
    return redirect('compartido')



def descargar_archivo_compartido(request, nombre_archivo):
    # Ruta base del archivo
    ruta_base = os.path.join('/home/pasix/Descargas/Pasix/Finalizado', nombre_archivo)  
    
    # Verificar si el archivo existe
    if os.path.exists(ruta_base):
        # Abrir el archivo y devolverlo como una respuesta de archivo
        with open(ruta_base, 'rb') as archivo:
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
            print("Ruta del archivo:", ruta_base)

            return response
    else:
        # Si el archivo no existe, devolver un error 404
        return HttpResponse(status=404)
