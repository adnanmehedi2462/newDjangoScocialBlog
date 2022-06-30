from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=False,blank=False)
    content=models.TextField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,upload_to='postimage/')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title