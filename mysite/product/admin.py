from django.contrib import admin
from product.models import Product, UserProfile, Alcohol

admin.site.register(Product)
admin.site.register(Alcohol)
admin.site.register(UserProfile)