from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreatrionForm(UserCreationForm):

    # valor = forms.ImageField(requiered=False)
    # valor = forms.texto(minval- max val)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


