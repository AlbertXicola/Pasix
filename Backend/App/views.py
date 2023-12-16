# views.py
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer