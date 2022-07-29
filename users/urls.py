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
    path('new-password',views.Another_Password,name='new-password')
]


