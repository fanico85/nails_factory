from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from insumos.models import Insumo
from servicios.models import Servicio
from gastos.models import Gasto
from atenciones.models import Atencion
from django.db.models import F
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#agregar como parametro de entrada en las clases basdas en vistas (LoginRequiredMixin,ListView)

@login_required
def inicio(request):   
    if request.method == "GET":

        #GASTOS        
        gastos = Gasto.objects.all()         
        suma = 0
        color_tarj_gastos = "card bg-primary text-white mb-4"        
       
        for gasto in gastos:                     
            suma += gasto.gas_monto     
        
        if suma > 700000 and suma < 720000:
            color_tarj_gastos = "card bg-warning text-white mb-4"
        elif suma > 720000:
            color_tarj_gastos = "card bg-danger text-white mb-4"

        #INSUMOS
        insumos =  Insumo.objects.filter(ins_stock_minimo__gte=F("ins_stock_actual"))
        cont_insumos = 0      
        cont_insumos = insumos.__len__() 
        color_tarj_insumo = "card bg-primary text-white mb-4"
        if cont_insumos > 0:
            color_tarj_insumo = "card bg-danger text-white mb-4"

        #SERVICIOS   
        servicios = Servicio.objects.all()
        cont_servicios = servicios.__len__()    

        #ATENCIONES   
        atenciones = Atencion.objects.all()
        cont_atenciones = atenciones.__len__()        

        return render(request, "core/index.html",
                      {"tarjeta_gasto_total":suma, 
                       "tarjeta_gasto_color":color_tarj_gastos, 
                       "tarjeta_servicio_cantidad":cont_servicios, 
                       "tabla_servicios":servicios, 
                       "tarjeta_insumo_color":color_tarj_insumo, 
                       "tarjeta_insumo_cantidad":cont_insumos,
                       "tarjeta_atenciones_realizadas":cont_atenciones
                       })

    return render(request, "core/index.html")

@login_required
def blanco(request):
    return render(request, "core/blanco.html")
