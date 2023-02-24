from rest_framework import serializers
from accounts.models import *
from products.models import *

class ProductMainSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductMain
        fields='__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'