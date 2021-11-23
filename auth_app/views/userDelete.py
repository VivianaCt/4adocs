from django.conf import settings 
from rest_framework import generics, status, views
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from auth_app.models.user import User 
from auth_app.serializers.userSerializer import UserSerializer 
 
class UserDelete(views.APIView):     
    queryset = User.objects.all()     
    serializer_class = UserSerializer     
    permission_classes = (IsAuthenticated,)   

    def delete(self, request, *args, **kwargs):
        #debe llegar PK del user y su accen token
        

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        userSerializer = UserSerializer()

        stringResponse = {'detail':'se elimino correctamente'}
        return Response(userSerializer.delete_element(id=kwargs["pk"]), status=status.HTTP_200_OK)
