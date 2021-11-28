from django.db import models


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length= 50)
    descripcion = models.CharField('descripcion', max_length= 400)
    precio = models.IntegerField('Precio Unitario', )
    stock = models.IntegerField('stock', )
    
    