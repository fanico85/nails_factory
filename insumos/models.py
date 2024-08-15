from django.db import models

# Create your models here.
class Marca(models.Model):
    mar_nombre = models.CharField(max_length=50, unique=True)
    mar_descripcion = models.CharField(max_length=100,null=True)
    mar_fecha_alta = models.DateTimeField(null=True)
    #mar_fecha_alta =  models.DateField(null=True,default=datetime.today)

    def get_nombre(self):
        return self.mar_nombre
    
    def get_descripcion(self):
        return self.mar_descripcion
    
    def get_fecha_alta(self):
        return self.mar_fecha_alta
    
    def __str__(self):
        return f"{self.mar_nombre}"




class Insumo(models.Model):
    ins_codigo = models.CharField(max_length=20, unique=True)
    ins_nombre = models.CharField(max_length=50)
    ins_marca = models.ForeignKey(Marca, on_delete=models.PROTECT)    
    ins_descripcion = models.CharField(max_length=100)
    ins_stock_actual = models.IntegerField(default=0)
    ins_stock_minimo = models.IntegerField(default=0)
    ins_stock_maximo = models.IntegerField(null=True, default=0)
    ins_unidad_medida = models.CharField(max_length=20)
    ins_contenido = models.IntegerField()    
 
    def get_codigo(self):
        return self.ins_codigo
    
    def get_nombre(self):
        return self.ins_nombre
    
    def get_marca(self):
        return self.ins_marca
    
    def get_stock_actual(self):
        return self.ins_stock_actual
    
    def get_stock_minimo(self):
        return self.ins_stock__minimo
    
    def get_stock_maximo(self):
        return self.ins_stock__maximo
    
    def get_unidad_medida(self):
        return self.ins_unidad_medida
    
    def get_contenido(self):
        return self.ins_contenido
    
    def get_descripcion(self):
        return self.ins_descripcion
    
    def __str__(self):
        return f"ID: {self.id} | Codigo: {self.ins_codigo} | Nombre: {self.ins_nombre} | Marca: {self.ins_marca} | Stock: {self.ins_stock_actual} | Unidad medida: {self.ins_unidad_medida} | Contenido: {self.ins_contenido} | Descripcion: {self.ins_descripcion}"


