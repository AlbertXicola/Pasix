from django.contrib import admin
from .models import Contacto
from .models import Fichero
from .models import Compartido

admin.site.register(Fichero)
admin.site.register(Contacto)
admin.site.register(Compartido)

