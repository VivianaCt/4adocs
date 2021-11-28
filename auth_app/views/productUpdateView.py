from django.conf import settings 
from rest_framework import generics, status, views
from rest_framework import permissions 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 

from auth_app.models.stock import Stock
from auth_app.serializers.stockSerializer import StockSerializer

class ProductUpdateView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])

        p = Stock(id = kwargs['pk'])

        productSerializer = StockSerializer(p, data=request.data)
        productSerializer.is_valid(raise_exception=True)
        updateProduct = productSerializer.save()

        return Response(productSerializer.to_representation(updateProduct), status=status.HTTP_200_OK)