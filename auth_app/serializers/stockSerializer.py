from rest_framework import serializers
from auth_app.models.stock import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['sku','nombre','descripcion','precio', 'stock']

    def create (self, validated_data):
        stockInstance= Stock.objects.create(**validated_data)
        return stockInstance

    def to_representation(self, obj):
        stock = Stock.objects.get(id=obj.id)
        return{
            'sku': stock.sku,
            'nombre': stock.nombre,
            'descripcion': stock.descripcion,
            'precio': stock.precio,
            'stock': stock.stock,
            
        }

    def delete_element(self, id):
        product = Stock.objects.get(sku=id),
        product.delete()

        return{
            'sku': product.sku,
            'nombre': product.nombre,
            'descripcion': product.descripcion,
            'precio': product.precio,
            'stock': product.stock,
        }

    def get_element(self, **obj):
        return Stock.objects.filter(**obj)
         