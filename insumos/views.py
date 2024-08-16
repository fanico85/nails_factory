from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from insumos.models import *
from insumos.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError

# Create your views here.
@login_required
def insumo_formulario(request):
    if request.method == "POST":
        mi_form = InsumoFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            insumo = Insumo(ins_codigo = info["insumo_codigo"],
                            ins_nombre = info["insumo_nombre"], 
                            ins_marca = info["insumo_marca"],
                            ins_descripcion = info["insumo_descripcion"],                             
                            ins_unidad_medida = info["insumo_unidad"],
                            ins_contenido = info["insumo_contenido"],
                            ins_stock_actual = info["insumo_stock_actual"],
                            ins_stock_minimo = info["insumo_stock_minimo"],
                            ins_stock_maximo = info["insumo_stock_maximo"])  
            try:
                insumo.save() 
                messages.success(request, "El producto fue creado correctamente") #success warning info error
                mi_form = InsumoFormulario()
            except Exception as err:
                messages.error(request, "Error al guardar el insumo, revisar los datos ingresados") #success warning info error

            return render(request, "insumos/crear.html", {"mi_formulario":mi_form})
    else:
        mi_form = InsumoFormulario()
        
    return render(request, "insumos/crear.html", {"mi_formulario":mi_form})


class InsumoListView(LoginRequiredMixin,ListView):
    model = Insumo
    context_object_name = "insumos"
    template_name = "insumos/listado.html"

class InsumoDeleteView(LoginRequiredMixin,DeleteView):
    model = Insumo
    template_name = "insumos/borrar.html"
    success_url = reverse_lazy('ListadoInsumos')
    

class InsumoUpdateView(LoginRequiredMixin,UpdateView):
    model = Insumo
    template_name = "insumos/modificar.html"
    success_url = reverse_lazy('ListadoInsumos')
    fields = ['ins_codigo', 'ins_nombre', 'ins_marca','ins_descripcion','ins_stock_actual','ins_stock_minimo','ins_stock_maximo','ins_unidad_medida','ins_contenido']


class MarcaListView(LoginRequiredMixin,ListView):
    model = Marca
    context_object_name = "marcas"
    template_name = "insumos/marcas/listado.html"
      
@login_required
def DeleteMarca(request,pk):

    item_to_delete = Marca.objects.get(pk=pk)
    nombre = item_to_delete.get_nombre()   
    try:
        item_to_delete.delete()
        messages.success(request, f"Se borró la marca {nombre} correctamente") #success warning info error
        
    except ProtectedError:
        messages.error(request, f"Error al borrar la marca {nombre}, ya que tiene Insumos asociados") #success warning info error
    except Exception:
        messages.error(request, f"Error al borrar la marca {nombre}") #success warning info error

    return render(request, "insumos/marcas/borrar.html")
         
 
class MarcaUpdateView(LoginRequiredMixin,UpdateView):
    model = Marca
    template_name = "insumos/marcas/modificar.html"
    success_url = reverse_lazy('ListadoMarcas')
    fields = ['mar_nombre','mar_descripcion']

@login_required
def marca_formulario(request):
    if request.method == "POST":
        mi_form = MarcaFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data            

            marca = Marca(mar_nombre = info["marca_nombre"],                            
                          mar_descripcion = info["marca_descripcion"])
            try:
                marca.save() 
                messages.success(request, f"La marca {marca.mar_nombre} fue creada correctamente") #success warning info error
                mi_form = MarcaFormulario()
            except Exception as err:
                messages.error(request, "Error al guardar la marca, revisar los datos ingresados") #success warning info error

            return render(request, "insumos/marcas/crear.html", {"mi_formulario":mi_form})
    else:
        mi_form = MarcaFormulario()
        
    return render(request, "insumos/marcas/crear.html", {"mi_formulario":mi_form})
 
