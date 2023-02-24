from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import *
from accounts.Serializer import *
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated 


# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class UserloginotpViewset(viewsets.ModelViewSet):
    queryset=Userloginotp.objects.all()
    serializer_class=UserloginotpSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class UserCartProductViewset(viewsets.ModelViewSet):
    queryset=UserCartProduct.objects.all()
    serializer_class=UserCartProductSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class UserCartViewset(viewsets.ModelViewSet):
    queryset=UserCart.objects.all()
    serializer_class=UserCartSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
