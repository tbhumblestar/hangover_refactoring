from django_filters import rest_framework as filters

from products.models import Product

class ProductListFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields={
            'price':['lt','gt'],
            'rating':['lt','gt'],
            'category__name':['iexact'],
            'name':['icontains'],
        }