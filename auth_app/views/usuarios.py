

from rest_framework import views, status, generics
from rest_framework.response import Response

from auth_app.models import User
from auth_app.serializers.userSerializer import UserSerializer

'''
    Crear usuarios
'''


class CrearUsuarioView(views.APIView):
    def get(self, request, *args, **kwargs):
        usuarios = User.objects.filter()
        tmp = []
        for u in usuarios:
            tmp.append(UserSerializer(u).data)
        return Response({
            'usuarios': tmp
        })

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        valid = serializer.is_valid()
        if valid:
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'mensaje'
            }, status=400)


class DetalleUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

