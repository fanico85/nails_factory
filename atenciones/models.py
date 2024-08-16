from django.db import models
from servicios.models import Servicio
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.
class Cliente(models.Model):
    cli_dni = models.IntegerField(unique=True)
    cli_nombre = models.CharField(max_length=50)
    cli_apellido = models.CharField(max_length=50)
    cli_celular = models.CharField(max_length=20)
    cli_email = models.EmailField(max_length=50,null=True)
    cli_red_social = models.CharField(max_length=50,null=True)
    cli_domicilio = models.CharField(max_length=100,null=True)
    cli_fecha_nacimiento = models.DateTimeField(null=True)
    cli_fecha_alta = models.DateTimeField(null=True)

    def get_dni(self):
        return self.cli_dni
    
    def get_nombre(self):
        return self.cli_nombre
    
    def get_apellido(self):
        return self.cli_apellido
    
    def get_celular(self):
        return self.cli_celular
    
    def get_email(self):
        return self.cli_email
    
    def get_red_social(self):
        return self.cli_red_social
    
    def get_domicilio(self):
        return self.cli_domicilio
    
    def get_fecha_nacimiento(self):
        return self.cli_fecha_nacimiento
    
    def get_fecha_alta(self):
        return self.cli_fecha_alta
    
    def __str__(self):
        return f"{self.cli_nombre} {self.cli_apellido}"

class FormaPago(models.Model):   
    fp_nombre = models.CharField(max_length=30, unique=True)
    fp_interes = models.DecimalField(max_digits=5,decimal_places=2)   

    def get_nombre(self):
        return self.fp_nombre
    
    def get_interes(self):
        return self.fp_interes
    
    def __str__(self):
        return f"{self.fp_nombre}"

class Atencion(models.Model):
    ate_numero = models.CharField(max_length=20, unique=True)
    ate_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)    
    ate_monto = models.DecimalField(max_digits=10,decimal_places=2)      
    ate_observacion = models.CharField(max_length=200, null=True)
    ate_fecha = models.DateField(null=True,default=datetime.today)
    ate_servicio = models.ForeignKey(Servicio, on_delete=models.RESTRICT) 
    ate_forma_pago = models.ForeignKey(FormaPago, on_delete=models.RESTRICT) 
    ate_cantidad = models.IntegerField(default=1)  
    ate_usuario = models.ForeignKey(User, on_delete=models.PROTECT) 
    ate_imagen = models.ImageField(upload_to="atenciones", blank=True, null=True)

    def get_numero(self):
        return self.ate_numero

    def get_cliente(self):
        return self.ate_cliente
    
    def get_monto(self):
        return self.ate_monto
    
    def get_observacion(self):
        return self.ate_observacion  
        
    def get_fecha(self):
        return self.ate_fecha  
    
    def get_servicio(self):
        return self.ate_servicio
    
    def get_forma_pago(self):
        return self.ate_forma_pago
    
    def get_cantidad(self):
        return self.ate_cantidad
    
    def get_usuario(self):
        return self.ate_usuario
    
    def get_imagen(self):
        return self.ate_imagen
       
    def __str__(self):
        return f"Numero: {self.ate_numero}"