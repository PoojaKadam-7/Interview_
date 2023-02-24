from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from accounts.views import *


router = routers.DefaultRouter()
router.register(r'accounts/user', UserViewset)
router.register(r'accounts/usercart', UserCartViewset)
router.register(r'accounts/userprofile', UserProfileViewset)
router.register(r'accounts/userloginotp', UserloginotpViewset)
router.register(r'accounts/usercartproduct', UserCartProductViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),

]
