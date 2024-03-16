from django.db import models

OPCIONES_CONSULTAS = [
    (0, "ㅤ  Seleccionar"),
    (1, "ㅤ  Sugerencias"),
    (2, "ㅤ  Ayuda"),
    (3, "ㅤ  Reportes"),
    (4, "ㅤ  Otros"),
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=OPCIONES_CONSULTAS[0:5], default=0)  
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre



class Fichero(models.Model):
    id_usuario = models.IntegerField(unique=False)
    id_archivo = models.CharField(max_length=255)
    hora_analizado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"ID_Archivo_Mongo: {self.id_archivo}, ID_Usuario: {self.id_usuario}, Hora analisis {self.hora_analizado}"


class Compartidos(models.Model):
    id_usuario = models.IntegerField(unique=False)
    id_ucompartido = models.IntegerField(unique=False)
    id_archivo = models.CharField(max_length=255)

    
    def __str__(self):
        return f"Ficheros compartidos por: {self.id_usuario}"




