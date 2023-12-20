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
client = pymongo.MongoClient("mongodb://pasix:20Logicalis21@172.27.64.1:27017/")
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó el archivo'}), 400
    
    file = request.files['file']
    # Asegurarse de que el directorio para analizar exista
    if not os.path.exists(carpeta_Para_analizar):
        os.makedirs(carpeta_Para_analizar)

    # Guardar el archivo en la carpeta para analizar
    archivo_path = os.path.abspath(os.path.join(carpeta_Para_analizar, file.filename))
    file.save(archivo_path)

    print(archivo_path)
    # Mover el archivo a la carpeta de análisis
    if os.path.exists(archivo_path):
        shutil.move(archivo_path, os.path.join(carpeta_Para_analizar, file.filename))
    
    sha256_hash = calcular_sha256_hash(archivo_path)

    resultado = collection.find_one({"Nuestro Hash": sha256_hash})

    if resultado:
        resultado['_id'] = str(resultado['_id'])
        return jsonify({'message': 'Datos encontrados en nuestra base de datos', 'data': resultado})

    response = enviar_a_virustotal(archivo_path)

    time.sleep(120)

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
                "Nombre Archivo": file.filename,
                "Nuestro Hash": sha256_hash,
                "id_API": vt_response["data"]["id"],
                "Antivirus Detectados": malicious_segunda_solicitud,
                "Prevision": mensaje_destino,
            }

            result = collection.insert_one(data_to_insert)
            data_to_insert['_id'] = str(result.inserted_id)

            if malicious_segunda_solicitud == 0:
                destino = ruta_destino_Limpio
            elif malicious_segunda_solicitud <= 5:
                destino = ruta_destino_Cuarentena
            elif malicious_segunda_solicitud > 5:
                destino = ruta_destino_Malicioso

            if not os.path.exists(os.path.join(destino)):
                os.makedirs(os.path.join(destino))

            shutil.move(archivo_path, os.path.join(destino, file.filename))

            mensaje = f'Datos agregados a la base de datos.'
            return jsonify({'message': mensaje, 'data': data_to_insert})

        else:
            return jsonify({'error': 'Error al obtener resultados de VirusTotal con el self.'}), 500

    else:
        return jsonify({'error': 'Error al enviar el archivo a VirusTotal.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    client.close()
