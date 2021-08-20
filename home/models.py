from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from PIL import Image
from annoying.fields import AutoOneToOneField

class Profile(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default = "No name")
    image = models.ImageField(default='../media/profile.jpg',upload_to='../media/')
    birth_date = models.DateField(null=True, blank=True) 
    phone = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f'{self.user.username} Profile'
    
        
    