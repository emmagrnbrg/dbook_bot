from django.contrib import admin

from .models import Category, Subcategory, Product, ProductSubcategory, ProductPhoto

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(ProductSubcategory)
admin.site.register(ProductPhoto)
