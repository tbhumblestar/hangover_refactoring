from rest_framework         import generics
from rest_framework.filters import OrderingFilter
from .models                import Product
from .serializers           import ProductSerializer
from django_filters         import rest_framework as filters
from core.filters import ProductListFilter

# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend,OrderingFilter]
    filterset_class = ProductListFilter
    ordering_fields =['rating']
    


