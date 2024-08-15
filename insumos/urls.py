from django.urls import path
from insumos import views

urlpatterns = [
    path('listado', views.InsumoListView.as_view(),name= "ListadoInsumos"),
    path('insumos/<pk>/borrar', views.InsumoDeleteView.as_view(),name= "BorrarInsumo"),
    path('insumos/<pk>/modificar', views.InsumoUpdateView.as_view(),name= "ModificarInsumo"),     
    path('insumos/nuevo', views.insumo_formulario,name= "NuevoInsumo"),
    path('marcas/listado', views.MarcaListView.as_view(),name= "ListadoMarcas"),
    #path('marcas/<pk>/borrar', views.MarcaDeleteView.as_view(),name= "BorrarMarca"),
    path('marcas/<pk>/borrar', views.DeleteMarca,name= "BorrarMarca"),    
    path('marcas/<pk>/modificar', views.MarcaUpdateView.as_view(),name= "ModificarMarca") , 
    path('marcas/nuevo', views.marca_formulario,name= "NuevoMarca"),
]