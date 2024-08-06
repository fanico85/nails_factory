from django.shortcuts import render

# Create your views here.
def inicio(request):   
    if request.method == "GET":

        #GASTOS
        print("llega")
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
        insumos =  Insumo.objects.filter(ins_stock__st_minimo__gte = F('ins_stock__st_actual'))
        cont_insumos = 0 
        print(cont_insumos)
        cont_insumos = insumos.__len__()     
        print(cont_insumos) 
        color_tarj_insumo = "card bg-primary text-white mb-4"

        if cont_insumos > 0:
            color_tarj_insumo = "card bg-danger text-white mb-4"

        #SERVICIOS   
        servicios = Servicio.objects.all()
        cont_servicios = servicios.__len__()
        print(cont_servicios)  

        return render(request, "Principal/index.html",{"tarjeta_gasto_total":suma, "tarjeta_gasto_color":color_tarj_gastos, "tarjeta_servicio_cantidad":cont_servicios, "tabla_servicios":servicios, "tarjeta_insumo_color":color_tarj_insumo, "tarjeta_insumo_cantidad":cont_insumos})

    return render(request, "Principal/index.html")
