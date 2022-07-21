from django.urls import path
from .views import about, event_booking, faq, home,contact, contact_success, privacy, refunds, tc, service, work

app_name = "home"

urlpatterns = [
    path('', home, name="index"),
    path('contact/', contact, name="contact"),
    path('contact-success/', contact_success, name="contactsuccess"),
    path('refunds/', refunds, name="refunds"),
    path('privacy/', privacy, name="privacy"),
    path('tc/', tc, name="tc"),
    path('service/', service, name="service"),
    path('about/', about, name="about"),
    path('faq/', faq, name="faq"),
    path('work/', work, name="work"),
    path('event-booking/', event_booking, name="event"),

]