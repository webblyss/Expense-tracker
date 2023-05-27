from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'You entered wrong credentials')
            
            return render(request,"login.html")
    
    
    return render(request,'login.html')





def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password != password2:
            messages.info(request,"password does not match")
            return render(request,"register.html")
        if User.objects.filter(email=email).exists():
            messages.info(request,"There is an account with the same email")
            return render(request,"register.html")
        
        if User.objects.filter(username=username).exists():
            messages.info(request,"There is an account with the username")
            return render(request,"register.html")

        new_user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        new_user.save()
        return redirect("login")
    
    return render(request,'register.html')





def user_logout(request):
    logout(request)
    
    return redirect('accounts:login_user')


