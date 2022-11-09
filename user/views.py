from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import models

# Create your views here.

def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home/')
        else: 
            return render(request, 'user/signup.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        
        exist_user = models.User.objects.filter(username=username)
        
        if exist_user:
            return render(request, 'user/signup.html')
        
        else:
            models.User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login/')

        
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('/home/')
        
        return render(request,'user/login.html')
        
    elif request.method == 'GET':
        user = request.user.is_authenticated
        
        if user:
             return redirect('/home/')
        
        return render(request,'user/login.html')
