from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gastos.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class GastoListView(LoginRequiredMixin,ListView):
    model = Gasto
    context_object_name = "gastos"
    template_name = "gastos/listado.html"

class GastoDeleteView(LoginRequiredMixin,DeleteView):
    model = Gasto
    template_name = "gastos/borrar.html"
    success_url = reverse_lazy('ListadoGastos')

class GastoUpdateView(LoginRequiredMixin,UpdateView):
    model = Gasto
    template_name = "gastos/modificar.html"
    success_url = reverse_lazy('ListadoGastos')
    fields = ['gas_nombre', 'gas_descripcion', 'gas_monto','gas_fecha']

class GastoDetailView(LoginRequiredMixin,DeleteView):
    model = Gasto
    template_name = "gastos/blanco.html"

class GastoCreateView(LoginRequiredMixin,CreateView):
    model = Gasto
    template_name = "gastos/crear.html"
    success_url = reverse_lazy('ListadoGastos')
    fields = ['gas_nombre', 'gas_descripcion', 'gas_monto','gas_fecha']


