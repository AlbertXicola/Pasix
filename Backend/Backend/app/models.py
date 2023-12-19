
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos adicionales que puedas necesitar

    def __str__(self):
        return self.user.username

opciones_consulta = [
    [0, "consulta"],
    [1, "hola"],
    [2, "sugerencia"],
    [3, "muertee"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta =models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
