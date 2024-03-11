from django.db import models

OPCIONES_CONSULTAS = [
    (0, "ㅤSeleccionar"),
    (1, "ㅤSugerencias"),
    (2, "ㅤAyuda"),
    (3, "ㅤReportes"),
    (4, "ㅤOtros"),
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
    id_archivo = models.CharField(max_length=255)  #habria que mirar que esto sea unico

    def __str__(self):
        return f"ID_Archivo_Mongo: {self.id_archivo}, ID_Usuario: {self.id_usuario}"




