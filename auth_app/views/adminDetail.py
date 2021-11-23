from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from auth_app.models.admins import Admin
from auth_app.serializers.adminSerializer import AdminSerializer 
 
class AdminDetail(generics.RetrieveAPIView):     
    queryset = Admin.objects.all()     
    serializer_class = AdminSerializer     
    permission_classes = (IsAuthenticated,)   

    def get(self, request, *args, **kwargs): 
       

        token = request.META.get('HTTP_AUTHORIZATION')[7:]         
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])         
        valid_data = tokenBackend.decode(token,verify=False) 
 
        if valid_data['admin_id'] != kwargs['pk']:             
            stringResponse = {'detail':'Unauthorized Request'}             
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)    

        return super().get(request, *args, **kwargs)