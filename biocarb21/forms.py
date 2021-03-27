from django import forms
from .models import Userbc21

class Userbc21Form1(forms.ModelForm):
    class Meta:
        model = Userbc21
        fields = ['nombre', 'email', 'telefono']
        widgets = {'nombre':forms.TextInput(attrs={'class': 'form-control border-radius input-verde', 'placeholder': 'Nombre completo:'}),
        'email':forms.TextInput(attrs={'class': 'form-control border-radius input-verde', 'placeholder': 'Email:'}),
        'telefono':forms.TextInput(attrs={'class': 'form-control border-radius input-verde', 'placeholder': 'Teléfono'}),
        }

class Userbc21Form2(forms.ModelForm):
    class Meta:
        model = Userbc21
        fields = ['nombre', 'email', 'telefono', 'fecha_nacimiento', 'genero', 'entidad_organizacion', 'cargo', 'departamento', 'municipio']
        #widgets = {'fecha_nacimiento': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}
        #'fecha_nacimiento':forms.SelectDateWidget(years=range(1900,2021)),
        widgets = {
        'fecha_nacimiento':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Fecha de nacimiento:', 'onfocus':"this.type='date'"}),
        'genero':forms.Select(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Fecha de nacimiento:'}),
        'entidad_organizacion':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Entidad/Organización:'}),
        'cargo':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Cargo:'}),
        'departamento':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Departamento:'}),
        'municipio':forms.TextInput(attrs={'class': 'form-control mb-3 input-verde', 'placeholder': 'Municipio:'}),
        }
