from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from app_product.models import ProductModel
from app_product.serializers import ProductSerializer


class ProductListForUserView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductListForAdminView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminUser]


class ProdictDetailForAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminUser]
