from rest_framework          import generics
from rest_framework.filters  import OrderingFilter
from rest_framework.response import Response
from .models                 import Product
from .serializers            import ProductSerializer
from django_filters          import rest_framework as filters
from core.paginations        import PagePagination
from core.filters            import ProductListFilter
from django.shortcuts        import get_object_or_404

# Create your views here.

class ProductListAPIView(generics.ListAPIView):
    pagination_class = PagePagination
    filter_backends  = [filters.DjangoFilterBackend,OrderingFilter]
    filterset_class  = ProductListFilter
    serializer_class = ProductSerializer
    queryset         = Product.objects.all()
    ordering         = ['-rating','price']
    ordering_fields  = ['rating','price']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        #dyanamic field filtering
        fields     = request.query_params.get('fields')
        if fields:
            fields = tuple(fields.split(','))
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True,fields=fields)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True,fields=fields)
        return Response(serializer.data)