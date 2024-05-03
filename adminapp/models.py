from django.db import models

# Create your models here.

class cred(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    u_type=models.CharField(max_length=100,default="user")
    u_status=models.CharField(max_length=100)

class user_det(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
    photo=models.ImageField(upload_to='user_images')
    username=models.CharField(max_length=100) 
