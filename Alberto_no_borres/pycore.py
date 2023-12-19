from flask import Flask, render_template, request, jsonify
import hashlib
import os
import requests
import pymongo
import time
import shutil
from bson import ObjectId  # Importa ObjectId desde el módulo bson

app = Flask(__name__)

carpeta_Para_analizar = "Para_Analizar"
ruta_destino_Limpio = "Finalizado/Limpio"
ruta_destino_Cuarentena = "Finalizado/Cuarentena"
ruta_destino_Malicioso = "Finalizado/Malicioso"

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://172.27.64.1:27017/")
db = client["Proyecto"]
collection = db["Archivos"]

# Clave de API de VirusTotal
api_key = "2f047d42c57a702fd720dd049e5d7f8d24baf8811faf42d34226e703be6270a9"
base_url = "https://www.virustotal.com/api/v3"

# Función para calcular el hash SHA-256 de un archivo
def calcular_sha256_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)  # Lee el archivo en bloques de 64 KB
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

# Función para enviar un archivo a VirusTotal v3
def enviar_a_virustotal(file_path):
    url = f"{base_url}/files"
    headers = {
        "x-apikey": api_key,
    }
    files = {"file": (file_path, open(file_path, "rb"))}
    response = requests.post(url, files=files, headers=headers)
    return response

# Función para obtener resultados de VirusTotal v3 utilizando la URL "self"
def obtener_resultados_virustotal(file_url):
    headers = {
        "x-apikey": api_key,
    }
    response = requests.get(file_url, headers=headers)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó el archivo'}), 400

    file = request.files['file']

    # Asegurarse de que el directorio exista
    if not os.path.exists(carpeta_Para_analizar):
        os.makedirs(carpeta_Para_analizar)

    # Guardar el archivo en la carpeta para analizar
    archivo_path = os.path.abspath(os.path.join(carpeta_Para_analizar, file.filename))
    file.save(archivo_path)

    sha256_hash = calcular_sha256_hash(archivo_path)

    # Buscar el hash en la base de datos
    resultado = collection.find_one({"Nuestro Hash": sha256_hash})

    if resultado:
        # Convertir el ObjectId a cadena antes de devolverlo como JSON
        resultado['_id'] = str(resultado['_id'])
        return jsonify({'message': 'Datos encontrados en nuestra base de datos', 'data': resultado})

    # Enviar el archivo a VirusTotal v3
    response = enviar_a_virustotal(archivo_path)

    time.sleep(120)

    if response.status_code == 200:
        vt_response = response.json()
        file_url = vt_response["data"]["links"]["self"]
        
        # Obtener resultados de VirusTotal utilizando la URL "self"
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

            # Agregar los datos a la base de datos
            data_to_insert = {
                "Nombre Archivo": file.filename,
                "Nuestro Hash": sha256_hash,
                "id_API": vt_response["data"]["id"],
                "Antivirus Detectados": malicious_segunda_solicitud,
                "Prevision": mensaje_destino,
            }
            # Inserta el documento y obtén el ObjectId generado
            result = collection.insert_one(data_to_insert)
            # Convierte el ObjectId a cadena antes de devolverlo como JSON
            data_to_insert['_id'] = str(result.inserted_id)

            if malicious_segunda_solicitud == 0:
                destino = ruta_destino_Limpio
            elif malicious_segunda_solicitud <= 5:
                destino = ruta_destino_Cuarentena
            elif malicious_segunda_solicitud > 5:
                destino = ruta_destino_Malicioso

            mensaje = f'Datos agregados a la base de datos.'
            return jsonify({'message': mensaje, 'data': data_to_insert})
        
            # Asegurarse de que el directorio destino exista
            if not os.path.exists(os.path.join(destino)):
                os.makedirs(os.path.join(destino))

            shutil.move(archivo_path, os.path.join(destino, file.filename))

            return jsonify({'message': 'Datos agregados a la base de datos.', 'data': data_to_insert})

        else:
            return jsonify({'error': 'Error al obtener resultados de VirusTotal con el self.'}), 500

    else:
        return jsonify({'error': 'Error al enviar el archivo a VirusTotal.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    client.close()
