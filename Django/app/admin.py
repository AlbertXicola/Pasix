from django.contrib import admin
from .models import Contacto
from .models import Fichero
from .models import Compartidos

admin.site.register(Fichero)
admin.site.register(Contacto)
admin.site.register(Compartidos)

