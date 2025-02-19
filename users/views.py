import json
import requests
import threading
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import VendorModel,CybersafeModel
from django.contrib.auth import authenticate, login
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


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
            request.session['username'] = username
           # print(request.session['username'])
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

@login_required
def Vendoriew(request):
        return render(request, "users/vendor.html")
# def checkauth():
#     return ( request.session['username']!=="")?"":render(request, "users/vendor.html")
@login_required
def VendorAuth(request):
    res = json.loads(request.body)
    event_name = res['name']
    email = res['email']
    categories = res['categories']
    phonenumber = res['phonenumber']
    lga = res['lga']
    experience = res['experience']
    residence = res['residence']
    if VendorModel.objects.filter(name=event_name).exists():
        return JsonResponse({"status":"exists"})
    else:
        v_save = VendorModel(name=event_name,email=email,phonenumber=phonenumber,categories=categories,lga=lga,experience=experience,residence=residence,)
        v_save.save()
        # details = VendorModel.objects.get(name=name)
        request.session['event_name'] = event_name
        # Vendorconfirm(event_name)
        return JsonResponse({"status": "success","event_name":event_name})


@login_required
def Vendorconfirm(request):
    event_name = request.GET['event_name']
    vendor = VendorModel.objects.get(name=event_name)
    context = {
                "vendor" : vendor
            }
    return render(request, "users/verify.html",context)



    #print(request.GET["event_name"])
    # if request.session.has_key('event_name') :
    #     name = request.session['event_name']
        
    #     vendor = VendorModel.objects.get(name=name)
    #     context = {
    #         vendor : vendor
    #     }
    #     return render(request, 'users/verify.html',context)
   # return render(request, 'users/verify.html')

def Profile(request):
    
    return render(request, 'users/profile.html')

def ProfileEdit(request):
    username = request.user.username
    detail = User.objects.get(username=username)
    context = {
        "detail" : detail
    }

    return render(request, 'users/edit-profile.html',context)

#=====CYBERSAFECAL PROPERTIES=====#
@csrf_exempt
def cybersafe(request):
    res = json.loads(request.body)
    email= res['email']
    message =res['message']
    subject = res['subject']
    if CybersafeModel.objects.filter(email=email).exists() and CybersafeModel.objects.filter(message=message).exists():
        return JsonResponse({"status":"alreadysent"})
    else:
        newm = CybersafeModel(email=email,message=message,subject=subject)
        newm.save()
        message2 = "MESSAGE:= " + message +"\n REPLY TO:=  " + email
        send_mail(
            subject,
            message2,
            'contact@cybersafecal.com',
            ['contact@cybersafecal.com'],
             fail_silently=False,
            )
            
           
        return JsonResponse({"status":"success"})
@csrf_exempt  
def anon_spammer(request):
    res = json.loads(request.body)
    message= res['message']
    count = 0
    limit = int(res['times'])
    link = res['link']
    for i in range(1,limit):
        count+=1
        response = requests.post(link, data={'message':f'{message}.{count}','btn-msg':''})
        if response.status_code == 200:
            print(f'message sent {count} times')
        else:
            print(response.status_code,link,message,)
            return JsonResponse({"status":response.status_code})
    # print("done")
    return JsonResponse({"status":"done"})   
    # print("done")



def anon_render(request):
    return render(request, 'core/anon.html')