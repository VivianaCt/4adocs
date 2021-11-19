from rest_framework import serializers
from auth_app.models.admins import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'nombre', 'email', 'password']

    def create (self, validated_data):
        adminInstance= Admin.objects.create(**validated_data)
        return adminInstance

    def to_representation(self, obj):
        admin = Admin.objects.get(id=obj.id)
        return{
            'id': admin.id,
            'nombre': admin.nombre,
            'email': admin.email,
            'password': admin.password,
    
            
        }
         