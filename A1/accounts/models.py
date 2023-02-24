from django.db import models
from products.models import *


class User(models.Model):
    Phone_number=models.CharField(max_length=12,unique=True)
    Email=models.EmailField(max_length=50)
    is_customer=models.BooleanField()
    is_admin=models.BooleanField()

class UserProfile(models.Model):
    owner=models.OneToOneField(User,on_delete=(models.CASCADE))
    Name=models.CharField(max_length=50)
    Date_of_birth=models.DateField()
    Gender=models.CharField(max_length=20,choices=(('Male','Male'),
                                                   ('Female','Female'),
                                                   ('Other','Other')))

    Image=models.ImageField()

class Userloginotp(models.Model):
    owner=models.ForeignKey(User,on_delete=(models.CASCADE))
    Otp=models.IntegerField()
    active=models.BooleanField()

class UserCartProduct(models.Model):
    Owner=models.ForeignKey(User,on_delete=(models.CASCADE))
    product=models.ForeignKey(ProductMain,on_delete=(models.CASCADE))
    status=models.CharField(max_length=20,choices=(('Pending','Pending'),
                                                   ('Completed','Completed')))

class UserCart(models.Model):
    owner=models.OneToOneField(User,on_delete=(models.CASCADE))
    product=models.ManyToManyField(UserCartProduct)
    price=models.IntegerField()


