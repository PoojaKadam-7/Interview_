from django.shortcuts import render
from rest_framework import viewsets
from products.models import *
from products.Serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProductMainViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=ProductMainSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class ProductImageViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=ProductImageSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]