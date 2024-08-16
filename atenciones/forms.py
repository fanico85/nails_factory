from django import forms
from atenciones.models import Cliente, User, Servicio, FormaPago
from django.utils.timezone import datetime

    
class FormaPagoFormulario(forms.Form):
    forma_pago_nombre = forms.CharField(max_length=50,label="Forma de Pago")
    forma_pago_interes = forms.DecimalField(max_digits=5,decimal_places=2,label="Interes") 

class ClienteFormulario(forms.Form):
    cliente_dni = forms.IntegerField(label="Documento")
    cliente_nombre = forms.CharField(max_length=50,label="Nombre")
    cliente_apellido = forms.CharField(max_length=50,label="Apellido")
    cliente_celular = forms.CharField(max_length=20,label="Celular")
    cliente_email = forms.EmailField(max_length=50,label="Email")
    cliente_red_social = forms.CharField(max_length=50,label="Red Social")
    cliente_domicilio = forms.CharField(max_length=100,label="Domicilio")
    cliente_fecha_nacimiento = forms.DateTimeField(label="Fecha Nacimiento")

class AtencionFormulario(forms.Form):
    atencion_numero = forms.CharField(max_length=20, label="Numero")
    atencion_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget= forms.Select(attrs={'class':'form-control'}),label="Cliente")
    atencion_monto = forms.DecimalField(max_digits=10,decimal_places=2, label="Monto Total")
    atencion_observacion = forms.CharField(max_length=200, label="Observacion",required=False)
    atencion_fecha = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date','value': datetime.today}),label="Fecha")
    atencion_servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), widget= forms.Select(attrs={'class':'form-control'}),label="Servicio")
    atencion_forma_pago = forms.ModelChoiceField(queryset=FormaPago.objects.all(), widget= forms.Select(attrs={'class':'form-control'}),label="Forma de Pago")
    atencion_cantidad =  forms.IntegerField(label="Cantidad")     
    atencion_usuario = forms.ModelChoiceField(queryset=User.objects.all(), widget= forms.Select(attrs={'class':'form-control'}),label="Usuario")
    atencion_imagen = forms.ImageField(label="Foto",required=False)
    

