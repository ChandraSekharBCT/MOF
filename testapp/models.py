from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	role=models.CharField(max_length=20,blank=True,null=True)

class Normal_User(models.Model):
	user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
	mobile=models.IntegerField()

class Whole_Seller(models.Model):
	user=models.ForeignKey(User,related_name="whole_seller",on_delete=models.CASCADE)
	city=models.CharField(max_length=200)
	mobile=models.IntegerField()
	zip_code=models.IntegerField()
	gst_no=models.CharField(max_length=100)
class Products(models.Model):
	user=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
	product_name=models.CharField(max_length=200)
	product_price=models.IntegerField()
	product_quantity=models.IntegerField()
	product_description=models.TextField()
	product_image=models.ImageField(upload_to='uploads/')
	product_image1=models.ImageField(upload_to='uploads/',blank=True,null=True)
	product_image2=models.ImageField(upload_to='uploads/',blank=True,null=True)
class Bank_Detail(models.Model):
	user=models.ForeignKey(User,related_name='bank_detail',on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	acc_no=models.IntegerField()
	ifcs_code=models.CharField(max_length=11)
	branch_name=models.CharField(max_length=200)
	bank_name=models.CharField(max_length=100)

