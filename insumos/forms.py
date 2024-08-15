from django import forms
from insumos.models import Marca

class InsumoFormulario(forms.Form):
    insumo_codigo = forms.CharField(max_length=20,label="Codigo")
    insumo_nombre = forms.CharField(max_length=50,label="Nombre")
    insumo_marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget= forms.Select(attrs={'class':'form-control'}),label="Marca")
    #forms.CharField(max_length=50,label="Marca")
    insumo_descripcion = forms.CharField(max_length=100,label="Descripción")    
    insumo_unidad = forms.CharField(max_length=20,label="Unidad de medida")
    insumo_contenido = forms.IntegerField(min_value=1, label="Contenido")
    insumo_stock_actual = forms.IntegerField(max_value=100, min_value=0, label="Stock inicial")
    insumo_stock_minimo = forms.IntegerField(max_value=100, min_value=0, label="Stock minimo")
    insumo_stock_maximo = forms.IntegerField(max_value=100, min_value=0, label="Stock maximo")

class MarcaFormulario(forms.Form):
    marca_nombre = forms.CharField(max_length=50,label="Nombre")
    marca_descripcion = forms.CharField(max_length=100,label="Descripción")    
    
    
