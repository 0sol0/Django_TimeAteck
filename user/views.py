from pickle import NONE
from django.shortcuts import render, redirect
from . import models

# Create your views here.

def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else: 
            return render(request, 'user/signup.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        
        exist_user = models.User().objects.filter(username=username)
        
        if exist_user:
            return render(request, 'user/signup.html')
        else:
            models.User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login')

        
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', NONE)
        password = request.POST.get('password', NONE)
        
        me = models.User.objects.get(username=username)
        if me.password == password:
            return redirect('/home')
        else:
            return redirect('/login')
            