from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicios.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ServicioListView(LoginRequiredMixin,ListView):
    model = Servicio
    context_object_name = "servicios"
    template_name = "servicios/listado.html"

class ServicioDeleteView(LoginRequiredMixin,DeleteView):
    model = Servicio
    template_name = "servicios/borrar.html"
    success_url = reverse_lazy('ListadoServicios')

class ServicioUpdateView(LoginRequiredMixin,UpdateView):
    model = Servicio
    template_name = "servicios/modificar.html"
    success_url = reverse_lazy('ListadoServicios')
    fields = ['ser_nombre', 'ser_descripcion', 'ser_duracion'] 

class ServicioDetailView(LoginRequiredMixin,DeleteView):
    model = Servicio
    template_name = "servicios/blanco.html"

class ServicioCreateView(LoginRequiredMixin,CreateView):
    model = Servicio
    template_name = "servicios/crear.html"
    success_url = reverse_lazy('ListadoServicios')
    fields = ['ser_nombre', 'ser_descripcion', 'ser_duracion']