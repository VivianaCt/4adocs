from auth_app.models.admins import Admin 
from auth_app.serializers.adminSerializer import AdminSerializer 

from django.conf import settings 
from rest_framework import generics, status, views
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 

class AdminDelete(views.APIView):     
    queryset = Admin.objects.all()     
    serializer_class = AdminSerializer     
    permission_classes = (IsAuthenticated,)   

    def delete(self, request, *args, **kwargs):
        #debe llegar PK del user y su accen token
        

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        adminSerializer = AdminSerializer()

        stringResponse = {'detail':'se elimino correctamente'}
        return Response(adminSerializer.delete_element(id=kwargs["pk"]), status=status.HTTP_200_OK)
      
