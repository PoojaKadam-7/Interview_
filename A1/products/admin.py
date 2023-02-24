from django.contrib import admin
from accounts.models import *
from products.models import *

@admin.register(ProductMain)
class ProductMainAdmin(admin.ModelAdmin):
    list_display=['Title','Description','Uique_id','Price']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display=['product','Image']