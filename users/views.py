from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User


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
            return render(request, 'users/sign-up.html')
    return render(request, 'users/sign-up.html')


def signup_done(request):
    return render(request, 'users/success-sign-up.html')

