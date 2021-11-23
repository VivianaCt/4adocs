from django.conf import settings 
from rest_framework import generics, status, views 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from auth_app.models.user import User 
from auth_app.serializers.userSerializer import UserSerializer 
 
class UserUpdate(generics.RetrieveAPIView):     
    queryset = User.objects.all()     
    serializer_class = UserSerializer     
    permission_classes = (IsAuthenticated,)   

    def put(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)                

        user = User( id = kwargs['pk'])

        userSerializer = UserSerializer(user, data=request.data)
        userSerializer.is_valid(raise_exception=True)        
        updatedUser= userSerializer.save()        

        return Response(userSerializer.to_representation(updatedUser), status=status.HTTP_200_OK)
        