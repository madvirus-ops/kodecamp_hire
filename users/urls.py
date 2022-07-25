from django.urls import  path
from . import views

app_name = 'users'

urlpatterns =[
    path('signup',views.signup,name='signup'),
    path('signup-done',views.signup_done,name='signup'),
    path('signin',views.signin,name='signin')
]


