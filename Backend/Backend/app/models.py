from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    #image = models.ImageField(upload_to="productos", null=True) #AGREGAR IMAGENES POR BASEDEDATOS


    def __str__(self):
        return self.nombre



opciones_consulta = [
    [0, "consulta"],
    [1, "hola"],
    [2, "sugerencia"],
    [3, "muertee"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=20)
    tipo_consulta =models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
