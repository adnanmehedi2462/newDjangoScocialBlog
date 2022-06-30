
from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="User_image", blank=False,null=False, default='default.png')
    bio=models.CharField(max_length=400,null=True,blank=True ,default="Please update your bio..!!")
    about=models.TextField(blank=True,null=True,  default="Please update your about..!!")
    def __str__(self):
        return self.user.first_name


