from django.db           import models
from core.models         import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.CharField(max_length=150)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    origin = models.ForeignKey('Origin',on_delete=models.CASCADE)
    img_url = models.CharField(max_length=300,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    
    def __str__(self):
        return f"{self.img_url}"
        # return f"{self.id} : {self.name}"
    
    class Meta:
        db_table = 'products'

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} : {self.name}"
    
    class Meta:
        db_table = 'categories'
    
class Origin(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} : {self.name}"
    
    class Meta:
        db_table = 'origins'
        

class WishList(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.nickname} : {self.product.name}"
    
    class Meta:
        db_table = 'wishlists'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'],
                name='user_product_unique_constraint')
        ]