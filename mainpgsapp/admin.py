from django.contrib import admin

from mainpgsapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)

