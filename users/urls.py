from django.urls import  path
from . import views
urlpatterns =[
    path('signup',views.signup,name='signup'),
    path('signup-done',views.signup_done,name='signup'),
]


