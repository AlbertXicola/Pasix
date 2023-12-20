from django.db import models

opciones_consultas = [
    [0, "Sugerencias"],
    [1, "Ayuda"],
    [2, "Reportes"],
    [3, "Más"],
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()


    def __str__(self):
        return self.nombre