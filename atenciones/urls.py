from django.urls import path
from atenciones import views

urlpatterns = [
    path('atenciones/listado', views.AtencionListView.as_view(),name= "ListadoAtenciones"),
    path('atenciones/<pk>/modificar', views.AtencionUpdateView.as_view(),name= "ModificarAtencion"),     
    path('atenciones/nuevo', views.atencion_formulario,name= "NuevoAtencion"),
    path('atenciones/<pk>', views.AtencionDetailView.as_view(),name= "DetalleAtencion"),
    path('atenciones/formapago/listado', views.FormaPagoListView.as_view(),name= "ListadoFormaPago"),
    path('atenciones/formapago/<pk>/borrar', views.DeleteFormaPago,name= "BorrarFormaPago"),    
    path('atenciones/formapago/<pk>/modificar', views.FormaPagoUpdateView.as_view(),name= "ModificarFormaPago") , 
    path('atenciones/formapago/nuevo', views.forma_pago_formulario,name= "NuevoFormaPago"),
    path('atenciones/cliente/listado', views.ClienteListView.as_view(),name= "ListadoCliente"),
    path('atenciones/cliente/<pk>/borrar', views.DeleteCliente,name= "BorrarCliente"),    
    path('atenciones/cliente/<pk>/modificar', views.ClienteUpdateView.as_view(),name= "ModificarCliente") , 
    path('atenciones/cliente/nuevo', views.cliente_formulario,name= "NuevoCliente"),
]


