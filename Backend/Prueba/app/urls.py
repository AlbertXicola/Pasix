from django.urls import path
from .views import home, contacto, galeria, registro, olvidada, terminos, user_view

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"), 
    path('galeria/', galeria, name="galeria"),
    path('registro', registro, name="registro"),
    path('olvidada/', olvidada, name='olvidada'),
    path('terminos/', terminos, name='terminos'),
    path('user/', user_view, name='user'),

    



]