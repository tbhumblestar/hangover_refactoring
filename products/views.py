from rest_framework             import generics
from rest_framework.filters     import OrderingFilter
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework             import status
from .models                    import (Product,
                                        WishList
                                        )
from django.shortcuts           import get_object_or_404
from django_filters             import rest_framework as filters
from core.paginations           import PagePagination
from core.filters               import ProductListFilter
from core.permissions           import DetailPermissionGetOrOnlyAdminOrOnlyWriter
from .serializers               import (ProductSerializer,
                                        WishlistSerializer
                                        )


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


class ProductDetailView(generics.RetrieveAPIView):
    queryset          = Product.objects.all()
    serializer_class  = ProductSerializer
    lookup_url_kwarg  = 'product_id'
    lookup_field      = 'id'

    
class WishlistCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class   = WishlistSerializer
    
    def create(self, request, *args, **kwargs):
        
        data = {
            "product" : self.kwargs.get('product_id'),
        }
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class WishlistDestroyView(generics.DestroyAPIView):
    permission_classes = [DetailPermissionGetOrOnlyAdminOrOnlyWriter]
    serializer_class   = WishlistSerializer
    queryset           = WishList.objects.all()
    lookup_url_kwarg  = 'wishlist_id'
    lookup_field      = 'id'
    

class WishlistUserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class   = WishlistSerializer
    queryset           = WishList.objects.all()
    lookup_url_kwarg  = 'user_id'
    lookup_field      = 'id'