from django.db import models

OPCIONES_CONSULTAS = [
    (0, "ㅤ"),
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


