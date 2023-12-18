from django.urls import path
from .views import home, terminos, olvidada, contacto, agregar_producto

urlpatterns = [
    path('', home, name='home'),
    path('terminos/', terminos, name='terminos'),
    path('olvidada/', olvidada, name='olvidada'),
    path('contacto/', contacto, name='contacto'),
    path('agregar_producto/', agregar_producto, name="agregar_producto")

]