from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Campo para almacenar la contraseña cifrada
    
    # Agrega otros campos según tus necesidades

    def save(self, *args, **kwargs):
        # Antes de guardar, cifra la contraseña si no está cifrada
        if not self.password.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):  
        return self.nombre
