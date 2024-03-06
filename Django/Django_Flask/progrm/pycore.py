from flask import Flask, render_template, request, jsonify
import hashlib
import os
import requests
import pymongo
import time
import shutil
from bson import ObjectId

app = Flask(__name__)

carpeta_Para_analizar = "Para_Analizar"
ruta_destino_Limpio = "Finalizado/Limpio"
ruta_destino_Cuarentena = "Finalizado/Cuarentena"
ruta_destino_Malicioso = "Finalizado/Malicioso"

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://pasix:20Logicalis21@127.0.0.1:27017/")
db = client["Proyecto"]
collection = db["Archivos"]

api_key = "2f047d42c57a702fd720dd049e5d7f8d24baf8811faf42d34226e703be6270a9"
base_url = "https://www.virustotal.com/api/v3"

def calcular_sha256_hash(file_path):
    sha256_hash = hashlib.sha256()
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
            last_analysis_stats = vt_response2.get("data", {}).get("attributes", {}).get("stats", {}).get("malicious", 0)
            malicious_segunda_solicitud = last_analysis_stats
            
            if malicious_segunda_solicitud == 0:
                destino = ruta_destino_Limpio
                mensaje_destino = 'Archivo limpio'
            elif malicious_segunda_solicitud <= 5:
                destino = ruta_destino_Cuarentena
                mensaje_destino = 'Archivo posiblemente infectado'
            elif malicious_segunda_solicitud > 5:
                destino = ruta_destino_Malicioso
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

from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

carpeta_Para_analizar = "ruta/a/tu/carpeta/para/analizar"

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No se proporcionaron archivos'}), 400

    archivos = request.files.getlist('files[]')

    if not archivos:
        return jsonify({'error': 'No se seleccionaron archivos válidos'}), 400

    # Asegurarse de que el directorio para analizar exista
    if not os.path.exists(carpeta_Para_analizar):
        os.makedirs(carpeta_Para_analizar)

    resultados = []  # Lista para almacenar resultados de los archivos subidos

    for archivo in archivos:
        archivo_path = os.path.abspath(os.path.join(carpeta_Para_analizar, archivo.filename))
        archivo.save(archivo_path)

        # Procesar el archivo y obtener el resultado específico
        resultado_procesamiento = procesar_archivo(archivo_path)

        # Agregar el resultado a la lista de resultados
        resultados.append(resultado_procesamiento)

    # Puedes devolver una respuesta JSON con los resultados de los archivos subidos
    print(resultados[0].get("data", {}))
    # En lugar de devolver JSON, renderiza un template de Django
    return render_template('test.html', message='Carga exitosa', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
