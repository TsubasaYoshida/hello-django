from django.contrib import admin

from .models import Brand, Product, Sku


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Sku)
