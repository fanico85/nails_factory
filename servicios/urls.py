from django.urls import path
from servicios import views

urlpatterns = [
    path('listado', views.ServicioListView.as_view(),name= "ListadoServicios"),
    path('servicios/<pk>/borrar', views.ServicioDeleteView.as_view(),name= "BorrarServicio"),
    path('servicios/<pk>/modificar', views.ServicioUpdateView.as_view(),name= "ModificarServicio") , 
    path('servicios/nuevo', views.ServicioCreateView.as_view(),name= "NuevoServicio"),    
    path('servicios/<pk>', views.ServicioDetailView.as_view(),name= "DetalleServicio"),
]
