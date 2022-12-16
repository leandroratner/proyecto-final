from django import forms
from ejemplo.models import Familiar, Vehiculo, Vacaciones, Mascota


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class VehiculoForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ["tipo", "color", "año_modelo"]

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ["tipo_animal", "edad"]

class VacacionesForm(forms.ModelForm):
  class Meta:
    model = Vacaciones
    fields = ["destino", "dias_de_estadia"]

class BuscarVehiculo(forms.Form):
    nombre = forms.CharField(max_length=50)

class BuscarMascota(forms.Form):
    nombre = forms.CharField(max_length=50)

class BuscarVacaciones(forms.Form):
    nombre = forms.CharField(max_length=50)

