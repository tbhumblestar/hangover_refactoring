from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    #원래라면 _category 혹은 category__name과 같은 식으로 해서, 해당 serializer를 활용한 create,update를 사용할 때, category나 origin이라는 이름이 겹쳐져서 발생하는 에러를 고려해야 하겠지만, 이 프로젝트에서는 어차피 Product를 Create,Update할 일이 없음
    category = serializers.CharField(source='category.name',read_only=True)
    origin = serializers.CharField(source='origin.name',read_only=True)
    
    def __init__(self,*args,**kwargs):
        print(kwargs)
        fields = kwargs.pop('fields',None)
        super().__init__(*args,**kwargs)
        
        print("self.fields : ",self.fields)
        
        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in (existing - allowed):

                self.fields.pop(field_name)
    
    class Meta:
        model = Product
        fields = '__all__'