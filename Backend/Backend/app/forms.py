from django import forms
from .models import Contacto, Producto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields ='__all__'  



class ProductoForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields ='__all__'  
   
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget
        }
