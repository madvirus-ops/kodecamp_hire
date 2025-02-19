from django.urls import  path
from . import views


app_name = 'users'

urlpatterns =[
    path('signup',views.signup,name='signup'),
    path('signup-done',views.signup_done,name='signup'),
    path('signin',views.signin,name='signin'),
    path('auth',views.Auth_User,name='auth'),
    path('authup',views.authup,name='authup'),
    path('reset-password',views.Password_Reset,name='reset-password'),
    path('new-password',views.Another_Password,name='new-password'),
    path('vendor-auth',views.VendorAuth,name='vendor-auth'),
    path('vendor-confirm',views.Vendorconfirm,name='vendor-confirm'),
    path('vendor',views.Vendoriew,name="vendor"),
    path('vendor/verify',views.Vendorconfirm,name='verify'),
    path('profile',views.Profile,name='profile'),
    path('profile/edit',views.ProfileEdit,name='profile-edit'),

]


