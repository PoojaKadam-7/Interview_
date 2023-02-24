from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from products.views import *

router = routers.DefaultRouter()
router.register(r'product/productmain', ProductMainViewset)
router.register(r'product/productimage', ProductImageViewset)


urlpatterns = [
    path('', include(router.urls)),
    
]
