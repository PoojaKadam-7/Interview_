from django.db import models

class ProductMain(models.Model):
	Title=models.CharField(max_length=100)
	Description=models.TextField(max_length=500)
	Uique_id=models.IntegerField(unique=True)
	Price=models.IntegerField()
	
class ProductImage(models.Model):
	product=models.ForeignKey(ProductMain,on_delete=(models.CASCADE))
	Image=models.ImageField()