from django.db import models


class Stock(models.Model):
    sku = models.IntegerField('Codigo',default=0)
    nombre = models.CharField('Nombre', max_length= 50)
    descripcion = models.CharField('descripcion', max_length= 400)
    precio = models.IntegerField('Precio Unitario', )
    stock = models.IntegerField('stock', )
    
    