from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def register(request):
    f1=forms.singininfo(data=request.POST)
    f2=forms.postinfo(data=request.POST)
    if f1.is_valid() and f2.is_valid():
        user = f1.save()
        user.set_password(user.password)
        user.save()
        profile = f2.save(commit=False)
        profile.user = user
        if 'profile_pic' in request.FILES:
            print('found it')
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        return redirect('/')
    return render(request,'singin.html',{'f1':f1,'f2':f2})

def log_in(request):
    log=forms.loginform()
    if request.method == 'POST':#
        log=forms.loginform(request.POST)
        if log.is_valid():
            user = authenticate(username=log.cleaned_data['username'],password=log.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('/')#HttpResponseRedirect(reverse('index'))
                else:

                    return HttpResponse('account is not active')
            else:

                return HttpResponse("details r not correct\n"+'username='+str(log.cleaned_data['username'])+
                '\npassword='+str(log.cleaned_data['password']))

    return render(request,'login.html',{'f1':log})
@login_required
def log_out(request):
    logout(request)
    return redirect('/')
