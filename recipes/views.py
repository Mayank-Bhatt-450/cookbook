from django.shortcuts import render,redirect
from recipes.models import *
from accounts.models import *
from . import forms
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,
                                View,
                                ListView,DetailView,
                                CreateView,DeleteView,UpdateView)

# Create your views here.
def search(request):
    if request.method == 'POST':
        obj=request.POST['txtSearch']
        search_result0=list(cuisines.objects.filter(cuisine_name__icontains=obj))
        search_result1=list(recipe.objects.filter(name__icontains=obj))+list(recipe.objects.filter(ingredients__icontains=obj))+list(recipe.objects.filter(method__icontains=obj))
        return render(
        request,
        'search_result.html',
        context={'search_result0':search_result0,'search_result1':search_result1})

def list_cuisines(request):
    return render(request,'cuisines_list.html',context={'cuisines_list':list(cuisines.objects.all())})
def list_recipe(request,cuisine_id):
    return render(request,'list_recipe.html',context={'recipe_list':list(cuisines.objects.filter(pk=str(cuisine_id))[0].all_recipe.all())})
def detail_recipe(request,recipe_id):
    tem=recipe.objects.filter(pk=str(recipe_id))[0]
    f1=forms.comment_form()
    f2=forms.note_form()
    user_name=request.user.username

    #'''
    if user_name !='':
        user_=User.objects.filter(username=user_name)[0]
        if request.method == 'POST':
            f1=forms.comment_form(request.POST)
            if f1.is_valid():
                print('\n\n\n\n------\n\n\n')
                obj_tem=commants(recipe=tem,
                user=user_,
                text=f1.cleaned_data['comment'])
                obj_tem.save()
        f1=forms.comment_form(initial={'comment':''})

        f2=''
        for i in user_.notes.all():
            if tem == i.recipe:
                f2=forms.note_form(initial={'note':i.note })
        if f2=='':
            f2=forms.note_form()

        if request.method == 'POST':
            f2=forms.note_form(request.POST)
            if f2.is_valid():

                obj_tem=note(recipe=tem,
                user=User.objects.filter(username=request.user.get_username())[0],
                note=f2.cleaned_data['note'])
                obj_tem.save()




    #tem=recipe.objects.filter(pk=str(recipe_id))[0]
    s=[]
    for i in list(tem.favorites.all()):
        s.append(i.username)
    return render(request,
    'detail_recipe.html',
    context={'recipe':tem,
            'ingredients':tem.ingredients.split('\n'),
            'method':tem.method.split('\n'),
            'comments':tem.commants.all(),
            'f1':f1,
            'f2':f2,
            'fav':s
            }
            )
def add_fav(request,id,usr):
    print('++++++++++++++\n\n\n')
    a=recipe.objects.filter(id=id)
    b=User.objects.filter(username=usr)
    print('++++++++++++++\n\n\n',a,b)
    if a!=[] and b!=[]:
        a=a[0]
        b=b[0]
        print('++++++++++++++\n\n\n',a.name,b.username)
        a.favorites.add(b)
        a.save()
        print(a.name,b.username,a.favorites.all())
    return HttpResponseRedirect('/detail/'+str(id))

def remove_fav(request,id,usr):
    a=recipe.objects.filter(id=id)
    b=User.objects.filter(username=usr)
    if a!=[] and b!=[]:
        a=a[0]
        b=b[0]
        a.favorites.remove(b)
    return HttpResponseRedirect('/detail/'+str(id))
def favorite_v(request,usr):
    obj = get_object_or_404(User, username=usr)
    return render(request,'list_recipe.html',context={'recipe_list':list(obj.favorites.all())})

def del_comment(request,pk,id):
    print(pk)
    aa='Deletion Confirm.'
    a=commants.objects.filter(id=pk)
    if a!=[]:
        a[0].delete()
    else:
        aa='Already Deleted.'
    return HttpResponseRedirect('/detail/'+str(id))


def autosuggest(request):
    obj=request.GET['term']
    qset=list(recipe.objects.filter(name__icontains=obj))
    result_list=[]
    result_list+=[x.name for x in qset]
    return JsonResponse(result_list,safe=False)
def del__note(request,pk):
    a=note.object.get(pk=pk)
    a.delete()
def create_recipe(request):
    f1=forms.recipe_form()
    if request.method == 'POST':
        f1=forms.recipe_form(request.POST)
        if f1.is_valid():
            rsp=f1.save(commit=False)
            if 'image' in request.FILES:
                rsp.image = request.FILES['image']
            rsp.save()
            return redirect('/')

    return render(request,
    'recipe_form.html',
    context={'f1':f1}
            )
def edit_recipe(request,pk):
    i=recipe.objects.filter(pk=pk)[0]
    f1=forms.recipe_edit_form(initial={'cuisine_name':i.cuisine_name,
                                    'name':i.name,
                                    'ingredients':i.ingredients,
                                    'method':i.method,
                                    'time':i.time })

    if request.method == 'POST':
        f1=forms.recipe_edit_form(request.POST)
        if f1.is_valid():
            rsp=f1.save(commit=False)
            if 'image' in request.FILES:
                rsp.image = request.FILES['image']
            rsp.save()
            return redirect('/')

    return render(request,
    'recipe_edit_form.html',
    context={'f1':f1}
                )
def del_recipe(request,pk):
    a=recipe.object.get(pk=pk)
    a.delete()
