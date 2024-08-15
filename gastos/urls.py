from django.urls import path
from gastos import views

urlpatterns = [
    path('listado', views.GastoListView.as_view(),name= "ListadoGastos"),
    path('gastos/<pk>/borrar', views.GastoDeleteView.as_view(),name= "BorrarGasto"),
    path('gastos/<pk>/modificar', views.GastoUpdateView.as_view(),name= "ModificarGasto") , 
    path('gastos/nuevo', views.GastoCreateView.as_view(),name= "NuevoGasto"),       
]
