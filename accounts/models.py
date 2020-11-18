from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_pic')
    profile_pic=models.ImageField(default='default_user.png')
