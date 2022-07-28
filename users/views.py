from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phonenumber = request.POST.get('phonenumber')
        check = request.POST.get('check')

        if password1 != password2:
            messages.error(request,'passwords do not match')
            return render(request, 'users/sign-up.html')
        else:
            new_user = User.objects.create_user(email=email,password=password2,username=name)
            new_user.save()
            messages.success(request,f'Account Created For {name}')
            return redirect('users:signin')
    return render(request, 'users/sign-up.html')


def signup_done(request):
    return render(request, 'users/success-sign-up.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #user = authenticate(username=username,password=password)
       # if User.objects.filter(username=username).exists():
        #    messages.success(request,"User Matched:)")
        #else:
         #   messages.error(request, "Email Address not Found")
          #  return redirect('users:signin')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username,password=password)    
            if user is not None:
                login(request, user)
                return redirect('core:home')
            else:
                messages.error(request, "username or password incorrect")
                return redirect('users:signin')
        else:
            messages.error(request,"user does not exist")
            return redirect('users:signin')
        
        
    return render(request, "users/login.html")

def Password_Reset(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        if User.objects.filter(email=Email).exists():
            messages.success(request, "email passed,Proceed")
            return redirect("users:new-password")
        else:
            messages.error(request, message="Email doesn't  exist")
            return redirect("users:reset-password")
    
    return render(request, "users/reset-password.html")

def Another_Password(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password1 = request.POST.get("password1")
        Password2 = request.POST.get("password2")
        if User.objects.filter(email=Email).exists() and Password1==Password2:
            user = User.objects.get(email=Email)
            user.set_password(Password2)
            user.save()
            messages.success("password reset succeeded, Login to continue")
            return redirect("users:login")
        else:
            messages.success(request,"passwords do not match")
            return redirect("users:new-password")
    return render(request, "users/new-password.html")