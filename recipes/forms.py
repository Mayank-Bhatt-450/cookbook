from django import forms
from django.contrib.auth.models import User
from . import models
class comment_form(forms.Form):
    comment=forms.CharField(required = True,max_length=400,widget=forms.Textarea
     (attrs={'class':'form-control ',
				   'id':'exampleFormControlTextarea1','rows':'1'}))

class note_form(forms.Form):
    note=forms.CharField(required = False,max_length=400,widget=forms.Textarea
    (attrs={'class':'form-control ',
                  'id':'exampleFormControlTextarea2','rows':'10'}))


class recipe_form(forms.ModelForm):
    class Meta():
        model = models.recipe
        fields = ('cuisine_name','name','ingredients','method','time','image')
        #exclude = ('cuisine_name')
    #comment=forms.CharField(max_length=400)
class recipe_edit_form(forms.ModelForm):
    class Meta():
        model = models.recipe
        fields = ('cuisine_name','name','ingredients','method','time')
        #exclude = ('cuisine_name')
    #comment=forms.CharField(max_length=400)
class search(forms.Form):
    txtSearch=forms.CharField(max_length=400)
