from django.contrib import admin
from products       import *
from products.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Origin)