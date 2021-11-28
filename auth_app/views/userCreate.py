from django.conf import settings
from rest_framework import status, views 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
 
from auth_app.serializers.userSerializer import UserSerializer  
 
class UserCreate(views.APIView): 
    #debe llegar JSON con la data del user a registrar

    def post(self, request, *args, **kwargs): 
        """
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """

        if(request.data['superuser']==""):
            request.data['superuser']='False'
        serializer = UserSerializer(data=request.data)         
        serializer.is_valid(raise_exception=True)         
        serializer.save() 

        tokenData = {"username":request.data["username"],                       
                     "password":request.data["password"]}         
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)         
        tokenSerializer.is_valid(raise_exception=True)                          
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        