from django.db import models

# Create your models here.
class Servicio(models.Model):
    ser_nombre = models.CharField(max_length=50, unique=True)
    ser_descripcion = models.CharField(max_length=100, default="descripcion")
    ser_duracion = models.IntegerField(default=10)  

    def get_nombre(self):
        return self.ser_nombre
    
    def get_descripcion(self):
        return self.ser_descripcion
    
    def get_duracion(self):
        return self.ser_duracion

    def __str__(self):
        return f"{self.ser_nombre}"