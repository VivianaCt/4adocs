from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from auth_app.models.admis import Admin
from auth_app.serializers.adminSerializer import AdminSerializer 
 
class AdminAllDetail(generics.RetrieveAPIView):     
    queryset = Admin.objects.all()     
    serializer_class = AdminSerializer     
    permission_classes = (IsAuthenticated,)   

    def get(self, request, *args, **kwargs):
        #debe llegar PK del user y su accen token
        #RETURN JSON con la data de todos los users

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['admin_id'] != kwargs['pk']:
            stringResponse = {'detail':'No está autorizado para ver esto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        adminSerializer = AdminSerializer()
        query_result = adminSerializer.get_element()

        result = []
        for admin in query_result:
            result.append(adminSerializer.to_representation(admin))

        return Response(result, status=status.HTTP_200_OK)