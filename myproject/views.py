from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def base(req):
    return render (req,'base.html')
def home(req):
    return render (req,'home.html')

def table(req):
    return render (req,'table.html')


def loginpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(password=password,username=username)

        if user:
            login(req,user)
            return redirect('base')

    return render (req,'loginpage.html')

def registerpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        user_type=req.POST.get('user_type')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            user=Custom_user.objects.create_user(user_type=user_type,username=username,password=confirm_password)
            return redirect('loginpage')
        else:
            return HttpResponse('password did not Matched')
    return render (req,'registerpage.html')
def logoutpage(req):
    logout(req)
    return redirect('loginpage')