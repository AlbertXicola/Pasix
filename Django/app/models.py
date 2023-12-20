from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="Productos", null=True)

    def __str__(self):
        return self.nombre
    



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