from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from auth_app.models.user import User 
from auth_app.models.serializers.userSerializer import UserSerializer 
 
class UserAllDetail(generics.RetrieveAPIView):     
    queryset = User.objects.all()     
    serializer_class = UserSerializer     
    permission_classes = (IsAuthenticated,)   

    def get(self, request, *args, **kwargs):
        #debe llegar PK del user y su accen token
        #RETURN JSON con la data de todos los users

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        userSerializer = UserSerializer()
        query_result = userSerializer.get_element()

        result = []
        for user in query_result:
            result.append(userSerializer.to_representation(user))

        return Response(result, status=status.HTTP_200_OK)