from django.contrib import admin
from products.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(WishList)