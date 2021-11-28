from rest_framework import serializers
from auth_app.models.user import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','telefono','direccion','password','superuser']

    def create(self, validated_data):
        if(validated_data['superuser']=='True'):
            userInstance = User.objects.create(**validated_data, is_superuser=True)
        else:
            userInstance = User.objects.create(**validated_data)
        
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        #account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'telefono': user.telefono, 
            'direccion': user.direccion,
            'password': user.password,
            
            }

    def get_element (self, **obj):
        return User.objects.filter(**obj)

    def delete_element(self, id):
        user=User.objects.get(id=id)
        user.delete ()
        return{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'telefono': user.telefono, 
            'direccion': user.direccion,
            'password': user.password,
        }    

