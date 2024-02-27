from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
    )

    email = forms.EmailField(
        label="Dirección de correo electrónico"
    )
     
    password1 = forms.CharField(
        label="Contraseña",

    )

    password2 = forms.CharField(
        label="Contraseña (confirmación)",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']