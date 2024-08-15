from django.db import models

# Create your models here.
class Gasto(models.Model):
    gas_nombre = models.CharField(max_length=50)
    gas_descripcion = models.CharField(max_length=100)
    gas_monto = models.DecimalField(max_digits=10,decimal_places=2)
    gas_fecha = models.DateField()

    def get_nombre(self):
        return self.gas_nombre
    
    def get_descripcion(self):
        return self.gas_descripcion
    
    def get_monto(self):
        return self.gas_monto
    
    def get_fecha(self):
        return self.gas_fecha

    def __str__(self):
        return f"ID: {self.id} | Gasto: {self.gas_nombre} | Descripcion: {self.gas_descripcion} | Monto $: {self.gas_monto} | Fecha: {self.gas_fecha}"
