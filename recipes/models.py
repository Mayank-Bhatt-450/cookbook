from django.db import models
from accounts.models import user_details , User
# Create your models here.
class cuisines(models.Model):
    cuisine_name=models.CharField(max_length=255)
    image=models.ImageField(default='default.jpg')
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.cuisine_name
class recipe(models.Model):
    cuisine_name=models.ForeignKey(cuisines,related_name='all_recipe', on_delete=models.CASCADE)
    name=models.CharField(max_length=400)
    ingredients= models.TextField()
    method= models.TextField()
    time=models.CharField(max_length=100)
    favorites=models.ManyToManyField(User,null=True, blank=True,related_name='favorites')
    image=models.ImageField(default='default.jpg')
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.name

    #commants
#'''
class commants(models.Model):
    recipe=models.ForeignKey(recipe,related_name='commants',on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    text=models.CharField(max_length=400,blank=False)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.text
#'''
class note(models.Model):
    recipe=models.ForeignKey(recipe,related_name='notes',on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User',related_name='notes',on_delete=models.CASCADE)
    note=models.CharField(max_length=400)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.note
#
