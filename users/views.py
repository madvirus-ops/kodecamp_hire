import json
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . import models 
from django.contrib.auth import authenticate, login
import sweetify
from django.http import JsonResponse 


# Create your views here.

def signup(request):
    # if request.method == 'POST':
        
    return render(request, 'users/sign-up.html')


def authup(request):
    res = json.loads(request.body)
    username = res['username']
    password1 = res['password1']
    password2 = res['password2']
    email = res['email']
    check = res['check']
    if password1 != password2:
            # sweetify.error(request,'passwords do not match')
            return JsonResponse({"status": "wrong"})
    else:
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "exists"})
        else:
            user = User.objects.create_user(username=username,password=password1,email=email)
            user.save()
            return JsonResponse({"status": "success"})


    # name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     phonenumber = request.POST.get('phonenumber')
    #     check = request.POST.get('check')

        
    #     else:
    #         new_user = User.objects.create_user(email=email,password=password2,username=name)
    #         new_user.save()
    #         sweetify.success(request,f'Account Created For {name}')
    #         return redirect('users:signin')

def signup_done(request):
    return render(request, 'users/success-sign-up.html')




def Auth_User(request):
    res = json.loads(request.body)
    username = res['username']
    password = res['password']
   # print(res);
    user = authenticate(username=username,password=password)
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username,password=password)    
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error"}) 
    else:
         return JsonResponse({"status": "User not Found.."}) 

def signin(request):        
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


def Vendoriew(request):
        return render(request, "users/vendor.html")

def VendorAuth(request):
    res = json.loads(request.body)
    name = res['name']
    email = res['email']
    categories = res['categories']
    phonenumber = res['phonenumber']
    lga = res['lga']
    experience = res['experience']
    residence = res['residence']
    if models.VendorModel.objects.filter(name=name).exists():
        return JsonResponse({"status":"exists"})
    else:
        v_save = models.VendorModel(name=name,email=email,phonenumber=phonenumber,categories=categories,lga=lga,experience=experience,residence=residence)
        v_save.save()
        # details = models.VendorModel.objects.get(name=name)
        return JsonResponse({"status": "success"})



def Vendorconfirm(request):
    res = json.loads(request.body)
    details = res['name']
    return JsonResponse({details:details})