from django.shortcuts import render, redirect
from .models import Event, Newsletter, Contact
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        if Newsletter.objects.filter(email=Email).exists():
            messages.error(request, "Already a Subscriber")
            return redirect("home:index")
        else:
            Email = request.POST.get("email")
            subscribe = Newsletter(email=Email)
            subscribe.save()
            messages.success(request, "Successfully subscribed")
            return redirect("home:index")

    return render(request, "home/index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phonecode = request.POST.get("phonecode")
        phone = request.POST.get("phone")
        message= request.POST.get("message")
        details = Contact(name = name, email = email, phonecode = phonecode, phone = phone, message = message)
        details.save()

        return redirect("home:contactsuccess")

    return render(request, "home/contact.html")


def event_booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        color = request.POST.get("color")
        location = request.POST.get("location")
        date = request.POST.get("date")
        time = request.POST.get("time")
        budget = request.POST.get("budget")
        eventtype = request.POST.get("eventtype")
        details= request.POST.get("details")
        event = Event(name = name, email = email, phone = phone, color=color, location=location, date=date,
        time = time, budget=budget, event_type=eventtype, details = details)
        event.save()

        messages.success(request, "Successfully booked an Event, We'll get in touch with you")
        return redirect("home:event")
    return render(request, "home/event-booking.html")

def contact_success(request):
    return render(request, "home/contact-success.html")

def refunds(request):
    return render(request, "home/refunds.html")

def privacy(request):
    return render(request, "home/privacy.html")

def tc(request):
    return render(request, "home/tc.html")

def service(request):
    return render(request, "home/service.html")

def about(request):
    return render(request, "home/about.html")

def faq(request):
    return render(request, "home/faq.html")

def work(request):
    return render(request, "home/work.html")