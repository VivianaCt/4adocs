from rest_framework import request, status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth_app.serializers.stockSerializer import StockSerializer

class ProductCreateView(views.APIView):

    def post(self, request, *arg, **kwargs):

        serializer = StockSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):

            p = serializer.save()

            return Response(serializer.to_representation(p), status=status.HTTP_201_CREATED)

        else:
            return Response("Error en la creacion", status=status.HTTP_400_BAD_REQUEST)