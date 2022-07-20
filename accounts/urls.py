from django.urls import path
from .views import booking, reset_password, new_password, vendor #account views
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    
    path('reset-password/', reset_password, name="reset-password"),
    path('new-password', new_password, name="new-password"),
    path('sign-up', views.signup,name='sign-up'),
    path('signup-done',views.signupDone,name='signup-done'),
    path('login/', views.signin, name="login"),
    path('vendor', vendor, name="vendor"),
    #path('verify', verify, name="verify"),
    path('booking', booking, name="booking"),
    #path('signout/', views.signout, name="signout"),
    path('signout/', auth_views.LogoutView.as_view(template_name ='accounts/signout.html'), name="signout"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)