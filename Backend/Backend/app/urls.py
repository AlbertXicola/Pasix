from django.urls import path
from .views import home, terminos, olvidada

urlpatterns = [
    path('', home, name='home'),
    path('terminos/', terminos, name='terminos'),
    path('olvidada/', olvidada, name='olvidada'),
    # Otros patrones de URL...
]