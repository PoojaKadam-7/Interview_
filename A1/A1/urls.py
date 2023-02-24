from django.contrib import admin
from django.urls import path,include
from accounts.urls import *
from products.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
]
