from django.contrib import admin
from .models import Product, ProductBacklogItem

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductBacklogItem)
