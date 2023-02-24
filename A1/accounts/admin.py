from django.contrib import admin
from accounts.models import *
# from products.models import *

# # Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['Phone_number','Email','is_customer','is_admin']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['owner','Name','Date_of_birth','Gender','Image']

@admin.register(Userloginotp)
class UserloginotpAdmin(admin.ModelAdmin):
    list_display=['owner','Otp','active']

@admin.register(UserCartProduct)
class UserCartProductAdmin(admin.ModelAdmin):
    list_display=['Owner','product','status']

# @admin.register(UserCart)
# class UserCartAdmin(admin.ModelAdmin):
#     list_display=['product','price']