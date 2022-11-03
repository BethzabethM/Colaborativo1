from django import forms
from ejemplo.models import (Familiar, Vivienda, Datos)

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento']

class ViviendaForm(forms.ModelForm):
  class Meta:
    model = Vivienda
    fields = ['nombre',  'tipo_casa', 'habitaciones', 'baños' ,'descripcion']

class DatosForm(forms.ModelForm):
  class Meta:
    model = Datos
    fields = ['nombre', 'profesion', 'hobbie', 'deporte']
