from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from catalog.api.filters import ProductFilter
from catalog.api.pagination import ProductPagination
from catalog.models import Product
from catalog.api.serializers import ProductListSerializer, ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
