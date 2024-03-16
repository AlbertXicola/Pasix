import os
import shutil
import time
from hashlib import sha256
from urllib.parse import urlencode
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from django.conf import settings

app_name = settings.APP_NAME

# Conexión a MongoDB
client = MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
db = client["Proyecto"]
collection = db["Archivos"]

api_key = "2f047d42c57a702fd720dd049e5d7f8d24baf8811faf42d34226e703be6270a9"
base_url = "https://www.virustotal.com/api/v3"

carpeta_Para_analizar = "Para_Analizar"
todos_los_archivos = "Finalizado"
#ruta_destino_Limpio = "Finalizado/Limpio"
#ruta_destino_Cuarentena = "Finalizado/Cuarentena"
#ruta_destino_Malicioso = "Finalizado/Malicioso"


def calcular_sha256_hash(file_path):
    sha256_hash = sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()


def enviar_a_virustotal(file_path):
    url = f"{base_url}/files"
    headers = {"x-apikey": api_key}
    files = {"file": (file_path, open(file_path, "rb"))}
    response = requests.post(url, files=files, headers=headers)
    return response


def obtener_resultados_virustotal(file_url):
    headers = {"x-apikey": api_key}
    response = requests.get(file_url, headers=headers)
    return response


def procesar_archivo(archivo_path):
    sha256_hash = calcular_sha256_hash(archivo_path)
    resultado = collection.find_one({"Our_Hash": sha256_hash})

    if resultado:
        resultado['_id'] = str(resultado['_id'])
        return {'message': 'Datos encontrados en nuestra base de datos', 'data': resultado}

    response = enviar_a_virustotal(archivo_path)
    time.sleep(15)

    if response.status_code == 200:
        vt_response = response.json()
        file_url = vt_response["data"]["links"]["self"]

        response2 = obtener_resultados_virustotal(file_url)

        if response2.status_code == 200:
            vt_response2 = response2.json()
            last_analysis_stats = vt_response2.get("data", {}).get("attributes", {}).get("stats", {}).get("malicious",0)
            malicious_segunda_solicitud = last_analysis_stats

            if malicious_segunda_solicitud == 0:
                destino = todos_los_archivos
                mensaje_destino = 'Archivo limpio'
            elif malicious_segunda_solicitud <= 5:
                destino = todos_los_archivos
                mensaje_destino = 'Archivo posiblemente infectado'
            elif malicious_segunda_solicitud > 5:
                destino = todos_los_archivos
                mensaje_destino = 'Archivo infectado'

            data_to_insert = {
                "Nombre_Archivo": os.path.basename(archivo_path),
                "Our_Hash": sha256_hash,
                "id_API": vt_response["data"]["id"],
                "Maldades": malicious_segunda_solicitud,
                "Prevision": mensaje_destino,
            }

            result = collection.insert_one(data_to_insert)
            data_to_insert['_id'] = str(result.inserted_id)

            if not os.path.exists(os.path.join(destino)):
                os.makedirs(os.path.join(destino))

            shutil.move(archivo_path, os.path.join(destino, os.path.basename(archivo_path)))

            mensaje = f'Datos agregados a la base de datos.'
            return {'message': mensaje, 'data': data_to_insert}

        else:
            return {'error': 'Error al obtener resultados de VirusTotal con el self.'}, 500

    else:
        return {'error': 'Error al enviar el archivo a VirusTotal.'}, 500


def procesar_archivos_en_carpeta():
    resultados = []
    archivos_a_procesar = os.listdir(carpeta_Para_analizar)

    for archivo_a_procesar in archivos_a_procesar:
        archivo_path = os.path.join(carpeta_Para_analizar, archivo_a_procesar)
        resultado_procesamiento = procesar_archivo(archivo_path)
        resultados.append(resultado_procesamiento)

    return resultados

