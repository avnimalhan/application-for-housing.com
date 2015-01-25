from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from myblog.models import *
from django import template
from django.contrib import auth
# Create your views here.
def showBlog(request):
    user=request.user
    blog=Article.objects.all()
    if request.user.is_authenticated():
        return render(request,'index.html',{'blog_list':blog,'user':user})
    else:
        return render(request,'login.html')
        
def signup(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password','')
        user = User.objects.create_user(username, email = email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.save()
        

        return HttpResponse('you have successfully registered')
    return render(request, 'signup.html')
def login(request):
    message='';
    if request.user.is_authenticated():
        return redirect('/')
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect('/')
        else:
            message='invalid username or password'
    return render(request,'login.html',{'message' : message})

def logout(request):
    auth.logout(request)
    return redirect('/')
    
        
    