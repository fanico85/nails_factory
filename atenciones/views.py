from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from atenciones.models import *
from atenciones.forms import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError
from django.db import IntegrityError

# Create your views here.
@login_required
def atencion_formulario(request):
    if request.method == "POST":
        mi_form = AtencionFormulario(request.POST,request.FILES) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            ate = info["atencion_numero"]

            atencion = Atencion(ate_numero = info["atencion_numero"],
                                ate_cliente = info["atencion_cliente"], 
                                ate_monto = info["atencion_monto"],
                                ate_observacion = info["atencion_observacion"],                             
                                ate_fecha = info["atencion_fecha"],
                                ate_servicio = info["atencion_servicio"],
                                ate_forma_pago = info["atencion_forma_pago"],
                                ate_cantidad = info["atencion_cantidad"],
                                ate_usuario = info["atencion_usuario"],
                                ate_imagen = info["atencion_imagen"])            
            try:
                atencion.save() 
                print("llegaaaa atencion")
                messages.success(request, f"Se registró la Atencion {ate}") #success warning info error
                mi_form = AtencionFormulario()
            except IntegrityError:
                messages.error(request, f"Error al registrar la atención, el numero de Atención ya existe") #success warning info error
            except Exception:
                messages.error(request, f"Error al registrar la atención, revisar los datos ingresados") #success warning info error

            return render(request, "atenciones/crear.html", {"mi_formulario":mi_form})
    else:
        mi_form = AtencionFormulario()
        
    return render(request, "atenciones/crear.html", {"mi_formulario":mi_form})


class AtencionListView(LoginRequiredMixin,ListView):
    model = Atencion
    context_object_name = "atenciones"
    template_name = "atenciones/listado.html"

class AtencionDetailView(LoginRequiredMixin,DetailView):
    model = Atencion   
    template_name = "atenciones/detalle.html"

class AtencionUpdateView(LoginRequiredMixin,UpdateView):
    model = Atencion
    template_name = "atenciones/modificar.html"
    success_url = reverse_lazy('ListadoAtenciones')
    fields = ['ate_fecha','ate_numero', 'ate_cliente', 'ate_servicio','ate_cantidad','ate_monto','ate_forma_pago','ate_usuario','ate_observacion','ate_imagen']

class FormaPagoListView(LoginRequiredMixin,ListView):
    model = FormaPago
    context_object_name = "formapagos"
    template_name = "atenciones/formapago/listado.html"

class FormaPagoUpdateView(LoginRequiredMixin,UpdateView):
    model = FormaPago
    template_name = "atenciones/formapago/modificar.html"
    success_url = reverse_lazy('ListadoFormaPago')
    fields = ['fp_nombre','fp_interes']

@login_required
def forma_pago_formulario(request):
    if request.method == "POST":
        mi_form = FormaPagoFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data            

            forma = FormaPago(fp_nombre = info["forma_pago_nombre"],                            
                                fp_interes = info["forma_pago_interes"])
            try:
                forma.save() 
                messages.success(request, f"La Forma de Pago {forma.fp_nombre} fue creada correctamente") #success warning info error
                mi_form = FormaPagoFormulario()
            except Exception as err:
                messages.error(request, "Error al guardar la Forma de Pago, revisar los datos ingresados") #success warning info error

            return render(request, "atenciones/formapago/crear.html", {"mi_formulario":mi_form})
    else:
        mi_form = FormaPagoFormulario()
        
    return render(request, "atenciones/formapago/crear.html", {"mi_formulario":mi_form})
    
@login_required
def DeleteFormaPago(request,pk):

    item_to_delete = FormaPago.objects.get(pk=pk)
    nombre = item_to_delete.get_nombre()   
    try:
        item_to_delete.delete()
        messages.success(request, f"Se borró la Forma de Pago: {nombre}") #success warning info error
        
    except ProtectedError:
        messages.error(request, f"Error al borrar la Forma de Pago: {nombre}. Tiene Atenciones asociadas") #success warning info error
    except Exception:
        messages.error(request, f"Error al borrar la Forma de Pago: {nombre}") #success warning info error

    return render(request, "atenciones/formapago/borrar.html")

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    context_object_name = "clientes"
    template_name = "atenciones/clientes/listado.html"

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "atenciones/clientes/modificar.html"
    success_url = reverse_lazy('ListadoCliente')
    fields = ['cli_dni','cli_nombre','cli_apellido','cli_celular','cli_email','cli_red_social','cli_domicilio','cli_fecha_nacimiento']

@login_required
def cliente_formulario(request):
    if request.method == "POST":
        mi_form = ClienteFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data            

            cliente = Cliente(cli_dni = info["cliente_dni"],                            
                            cli_nombre = info["cliente_nombre"],
                            cli_apellido = info["cliente_apellido"],
                            cli_celular = info["cliente_celular"],
                            cli_email = info["cliente_email"],
                            cli_red_social = info["cliente_red_social"],
                            cli_domicilio = info["cliente_domicilio"],
                            cli_fecha_nacimiento = info["cliente_fecha_nacimiento"])
            try:
                cliente.save() 
                messages.success(request, f"Se registró correctamente a {cliente.cli_nombre} {cliente.cli_apellido}") #success warning info error
                mi_form = ClienteFormulario()
            except Exception as err:
                messages.error(request, "Error al guardar el cliente, revisar los datos ingresados") #success warning info error

            return render(request, "atenciones/clientes/crear.html", {"mi_formulario":mi_form})
    else:
        mi_form = ClienteFormulario()
        
    return render(request, "atenciones/clientes/crear.html", {"mi_formulario":mi_form})
    
@login_required
def DeleteCliente(request,pk):

    item_to_delete = Cliente.objects.get(pk=pk)
    nombre = item_to_delete.get_nombre()
    apellido = item_to_delete.get_apellido()   
    try:
        item_to_delete.delete()
        messages.success(request, f"Se borró a {nombre} {apellido}") #success warning info error
        
    except ProtectedError:
        messages.error(request, f"Error al borrar el cliente. Tiene Atenciones asociadas") #success warning info error
    except Exception:
        messages.error(request, f"Error al borrar el cliente") #success warning info error

    return render(request, "atenciones/clientes/borrar.html")
         
 



 

