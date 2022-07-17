from rest_framework         import generics
from rest_framework.filters import OrderingFilter
from .models                import Product
from .serializers           import ProductSerializer
from django_filters         import rest_framework as filters
from core.paginations       import PagePagination
from core.filters           import ProductListFilter
from django.shortcuts       import get_object_or_404

# Create your views here.

class ProductListAPIView(generics.ListAPIView):
    pagination_class = PagePagination
    filter_backends  = [filters.DjangoFilterBackend,OrderingFilter]
    filterset_class  = ProductListFilter
    serializer_class = ProductSerializer
    queryset         = Product.objects.all()
    ordering         = ['-rating','price']
    ordering_fields  = ['rating','price']