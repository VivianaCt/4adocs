from django.conf import settings
from rest_framework import status, views 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
 
from auth_app.serializers.adminSerializer import AdminSerializer  
 
class AdminCreate(views.APIView): 
    #debe llegar JSON con la data del user a registrar

    def post(self, request, *args, **kwargs): 
        
        serializer = AdminSerializer(data=request.data)         
        serializer.is_valid(raise_exception=True)         
        serializer.save() 

        tokenData = {"nombre":request.data["nombre"],                       
                     "password":request.data["password"]}         
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)         
        tokenSerializer.is_valid(raise_exception=True)                          
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)