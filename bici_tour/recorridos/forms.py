from django import forms
from .models import Preinscripcion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Preinscripcion
        fields = ['nombre', 'correo', 'telefono', 'ciudad', 'estado']
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "correo": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "ciudad": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),

        }