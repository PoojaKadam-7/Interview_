from rest_framework import serializers
from accounts.models import *
from products.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

class UserloginotpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userloginotp
        fields='__all__'

class UserCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCartProduct
        fields='__all__'

class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCart
        fields='__all__'