from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'GET':
        if request.user.is_annonymous:
            return redirect('/login/')
        
        return render(request, 'sparta/home.html') 