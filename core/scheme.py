from rest_framework  import serializers
from products.models import Product


class ProductSearchScheme(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','name']
        ref_name = 'product_info'
        
class ProductSearchMainScheme(serializers.Serializer):
    products_by_name = ProductSearchScheme(many=True)
    products_by_category = ProductSearchScheme(many=True)

    class Meta:
        ref_name = 'searched_products'

class KaoKaoLoginJWTScheme(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    
    class Meta:
        ref_name = 'jwt'

class KaoKaoLoginMainScheme(serializers.Serializer):
    nickname = serializers.CharField()
    email    = serializers.CharField()
    id       = serializers.IntegerField()
    jwt      = KaoKaoLoginJWTScheme()