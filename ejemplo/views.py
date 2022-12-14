from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Vehiculo, Mascota, Vacaciones
from ejemplo.models import MVPFamiliares
from ejemplo.forms import Buscar, FamiliarForm, BuscarMascota, BuscarVacaciones, BuscarVehiculo # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request, "ejemplo/saludar_a.html", 
    {"nombre" :nombre}) 

def sumar(request, a, b):
    return render(request, "ejemplo/sumar.html",
    {"a": a,
     "b": b,
    "resultado": a + b
    }
    )

def buscar(request):
    lista_de_nombres = ["Pedro","Jorge","Leo"]
    query = request.GET['q']
    if query in lista_de_nombres:
        indice_de_resultado = lista_de_nombres.index(query)
        resultado = lista_de_nombres[indice_de_resultado]
    else:
        resultado = "no hay match"

    return render(request, 'ejemplo/buscar.html',
    {"resultado": resultado})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_familiaresMVP(request):
  lista_familiaresMVP = MVPFamiliares.objects.all()
  return render(request, "ejemplo/MVP_familiares.html", {"lista_familiaresMVP": lista_familiaresMVP})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con ??xito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atenci??n ahora el method get recibe un parametro pk == primaryKey == identificador ??nico
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atenci??n ahora el method post recibe un parametro pk == primaryKey == identificador ??nico
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualiz?? con ??xito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class FamiliarList(DetailView):
     model = Familiar
class FamiliarList(ListView):
  model = Familiar
class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]
class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"
class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/success_update_messagge"
    fields = ["nombre", "direccion", "numero_pasaporte"]




class VehiculoList(ListView):
    model = Vehiculo
class VehiculoCrear(CreateView):
    model = Vehiculo
    success_url = "/panel-vehiculo"
    fields = ["tipo", "color", "a??o_modelo"]
class VehiculoBorrar(DeleteView):
    model = Vehiculo
    success_url = "/panel-vehiculo"
class VehiculoActualizar(UpdateView):
    model = Vehiculo
    success_url = "/panel-vehiculo"
    fields = ["tipo", "color", "a??o_modelo"]

class MascotaList(ListView):
    model = Mascota
class MascotaCrear(CreateView):
    model = Mascota
    success_url = "/panel-mascota"
    fields = ["tipo_animal", "edad"]
class MascotaBorrar(DeleteView):
    model = Mascota
    success_url = "/panel-mascota"
class MascotaActualizar(UpdateView):
    model = Mascota
    success_url = "/panel-mascota"
    fields = ["tipo_animal", "edad"]

class VacacionesList(ListView):
    model = Vacaciones
class VacacionesCrear(CreateView):
    model = Vacaciones
    success_url = "/panel-vacaciones"
    fields = ["destino", "dias_de_estadia"]
class VacacionesBorrar(DeleteView):
    model = Vacaciones
    success_url = "/panel-vacaciones"
class VacacionesActualizar(UpdateView):
    model = Vacaciones
    success_url = "/panel-vacaciones"
    fields = ["destino", "dias_de_estadia"]

class BuscarVacaciones(View):
    form_class = BuscarVacaciones
    template_name = 'ejemplo/vacaciones_buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_vacaciones = Vacaciones.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vacaciones':lista_vacaciones})
        return render(request, self.template_name, {"form": form})

class BuscarVehiculo(View):
    form_class = BuscarVehiculo
    template_name = 'ejemplo/vehiculo_buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_vehiculos = Vehiculo.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vehiculos':lista_vehiculos})
        return render(request, self.template_name, {"form": form})

class BuscarMascota(View):
    form_class = BuscarMascota
    template_name = 'ejemplo/mascotas_buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})