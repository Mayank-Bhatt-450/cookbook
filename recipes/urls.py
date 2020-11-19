"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from recipes import views
from django.contrib import admin
app_name = 'goto'
urlpatterns = [
    path('dfdsfdsf', views.admins,name='admins'),
    path('', views.list_cuisines,name='home'),
    path('cuisine_id_<cuisine_id>', views.list_recipe,name='cuisine'),
    path('detail/<recipe_id>', views.detail_recipe,name='detail_recipe'),
    path('search',views.search,name='search'),
    path('create_recipe/',views.create_recipe,name='create_recipe'),
    path('edit_recipe/<pk>',views.edit_recipe,name='edit_recipe'),
    path('autosuggest',views.autosuggest,name='autosuggest'),
    path('del_comment/<pk>/<id>', views.del_comment,name='del_comment'),
    path('add_fav/<id>/<usr>', views.add_fav,name='add_fav'),
    path('remove_fav/<id>/<usr>', views.remove_fav,name='remove_fav'),
    path('favorite_<usr>', views.favorite_v,name='favorite_v'),
]
