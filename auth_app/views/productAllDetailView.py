from django.conf import settings 
from rest_framework import generics, serializers, status, views
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 

from auth_app.models.stock import Stock
from auth_app.serializers.stockSerializer import StockSerializer

class ProductAllDetailView(views.APIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        productSerializer = StockSerializer()
        query_result = productSerializer.get_element()

        result = []

        for product in query_result:
            result.append(productSerializer.to_representation(product))

        return Response(result, status=status.HTTP_200_OK)

