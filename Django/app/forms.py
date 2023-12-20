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
        widget=forms.PasswordInput,
        help_text="La contraseña debe contener al menos un carácter '@'."
    )

    password2 = forms.CharField(
        label="Contraseña (confirmación)",
        widget=forms.PasswordInput,
    )

    def clean_password1(self):
        # Validación personalizada para asegurarse de que la contraseña contenga '@'
        password1 = self.cleaned_data.get("password1")
        if "@" not in password1:
            raise forms.ValidationError("La contraseña debe contener al menos un carácter '@'.")
        return password1

    def clean_password2(self):
        # Verifica si las dos entradas de contraseña coinciden
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']