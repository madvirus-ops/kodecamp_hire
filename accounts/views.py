
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from accounts.models import User_Number, Vendor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def reset_password(request):
	if request.method == "POST":
		Email = request.POST.get("email")
		if User.objects.filter(email=Email).exists():
			return redirect("accounts:new-password")
		else:
			messages.error(request, message="User does not exist")
			return redirect("accounts:reset-password")

	return render(request, "accounts/reset-password.html")

def new_password(request):
	if request.method == "POST":
		Email = request.POST.get("email")
		Password1 = request.POST.get("password1")
		Password2 = request.POST.get("password2")
		if User.objects.filter(email=Email).exists() and Password1==Password2:
			user = User.objects.get(email=Email)
			user.set_password(Password2)
			user.save()
            
			return redirect("accounts:login")
		else:
            
			return redirect("accounts:new-password")
			
	return render(request, "accounts/new-password.html")


# Create your views here.

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phoneNumber')
        password1 = request.POST.get('password1')
        check = request.POST.get('check1')
        password2 = request.POST.get('password2')
        #checking if user already exists 
        if User.objects.filter(username=email).exists():
            messages.success(request,"User Already Exists :)")
            return render(request, 'accounts/success-sign-up.html')
        else:
            if password2 == password1:
                new_user = User.objects.create_user(username=email,email=email,password=password2,
                                                    first_name=firstname,last_name=lastname)
                user_phone = User_Number(number=phonenumber,user=new_user,terms=check)
                user_phone.save()
                new_user.save()
                messages.success(request,f'Account created for {firstname}')
                return render(request, 'accounts/success-sign-up.html')
    else:
        return render(request, "accounts/sign-up.html")


def signupDone(request):
    return render(request, 'accounts/success-sign-up.html')

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if User.objects.filter(username=username).exists():
            messages.success(request,"User Matched:)")
        else:
            messages.error(request, "Email Address not Found")
            return redirect('accounts:login')
        user = authenticate(username=username,password=password)    
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, "username or password incorrect")
            return redirect('accounts:sign-up')
        
        
    return render(request, "accounts/login.html")

def vendor(request):
    if request.method == "POST":
        user=request.user
        vendor_name = request.POST.get("name")
        vendor_email = request.POST.get("email")
        vendor_phonecode = request.POST.get("phonecode")
        vendor_phone = request.POST.get("phone")
        vendor_category = request.POST.get("categories")
        vendor_address = request.POST.get("address")
        vendor_state = request.POST.get("state")
        vendor_lga = request.POST.get("lga")
        vendor_experience = request.POST.get("experience")
        new_vendor = Vendor(user=user, name=vendor_name, email=vendor_email, phonecode=vendor_phonecode, phone=vendor_phone, 
            categories=vendor_category, address=vendor_address, statec=vendor_state, lga=vendor_lga, experience=vendor_experience)
        new_vendor.save()
        
        verified = Vendor.objects.get( name = vendor_name)
        context = {
           "verified" : verified
        }

        return render(request, "accounts/verify.html", context)   
        #return redirect('accounts:verify', context)

    return render(request, "accounts/vendor.html")


def booking(request):
    return render(request, 'accounts/booking.html')
