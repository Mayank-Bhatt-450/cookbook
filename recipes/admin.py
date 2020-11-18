from django.contrib import admin

# Register your models here.
from recipes.models import *
# Register your models here.
admin.site.register(cuisines)
admin.site.register(recipe)
admin.site.register(commants)
admin.site.register(note)
