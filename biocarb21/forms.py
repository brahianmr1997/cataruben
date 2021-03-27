from django import forms
from .models import Userbc21

class Userbc21Form(forms.ModelForm):
    class Meta:
        model = Userbc21
        fields = ['nombre', 'email', 'telefono', 'fecha_nacimiento', 'genero', 'entidad_organizacion', 'cargo', 'departamento', 'municipio']
        #widgets = {'fecha_nacimiento': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}
        #'fecha_nacimiento':forms.SelectDateWidget(years=range(1900,2021)),
        widgets = {
        'fecha_nacimiento':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Fecha de nacimiento:', 'onfocus':"this.type='date'", 'required':'true'}),
        'genero':forms.Select(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'genero:', 'required':'true'}),
        'entidad_organizacion':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Entidad/Organización:', 'required':'true'}),
        'cargo':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Cargo:', 'required':'true'}),
        'departamento':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Departamento:',  'required':'true'}),
        'municipio':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Municipio:', 'required':'true'}),
        }
