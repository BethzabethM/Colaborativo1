from django.shortcuts import render
from django.shortcuts import render
from ejemplo.models import (Familiar, Datos, Vivienda, Configuracion)
from ejemplo.forms import (Buscar, FamiliarForm, ViviendaForm, DatosForm)
from django.views import View 


# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html", 
    {"nombre":"German",
    "apellido":"Martinez"})

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", 
    {"nombre":nombre,
    "apellido":apellido})

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7]}
    )

def imc(request, peso, altura):
    imc = int(peso) * float(altura)
    return render(request, "ejemplo/imc.html", {"imc":imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_un_solo_familiar(request, id):
    identificador = int(id)
    return render(request, "ejemplo/un_familiar.html", Familiar.objects.get(id=identificador))


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        conf_pages = Configuracion.objects.first()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form, 'conf_pages':conf_pages})

    def post(self, request):
        conf_pages = Configuracion.objects.first()
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares,
                                                        'conf_pages':conf_pages})
        return render(request, self.template_name, {"form": form, 'conf_pages':conf_pages})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        conf_pages = Configuracion.objects.first()
        return render(request, self.template_name, {'form':form,'conf_pages':conf_pages})

    def post(self, request):
        form = self.form_class(request.POST)
        conf_pages = Configuracion.objects.first()
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito,
                                                        'conf_pages':conf_pages})
        
        return render(request, self.template_name, {"form": form, 'conf_pages':conf_pages}) 


class Datos(View):
    form_class = DatosForm
    template_name = 'ejemplo/datos_familiar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        conf_pages = Configuracion.objects.first()
        return render(request, self.template_name, {'form':form,'conf_pages':conf_pages})

    def post(self, request):
        form = self.form_class(request.POST)
        conf_pages = Configuracion.objects.first()
        if form.is_valid():
            form.save()
            msg_exito = f"Se actualizó con éxito  {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito,
                                                        'conf_pages':conf_pages})
        
        return render(request, self.template_name, {"form": form, 'conf_pages':conf_pages})

class Vivienda(View):
    form_class = ViviendaForm
    template_name = 'ejemplo/vivienda_familiar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        conf_pages = Configuracion.objects.first()
        return render(request, self.template_name, {'form':form,'conf_pages':conf_pages})

    def post(self, request):
        form = self.form_class(request.POST)
        conf_pages = Configuracion.objects.first()
        if form.is_valid():
            form.save()
            msg_exito = f"Se actualizó con éxito  {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito,
                                                        'conf_pages':conf_pages})
        
        return render(request, self.template_name, {"form": form, 'conf_pages':conf_pages})