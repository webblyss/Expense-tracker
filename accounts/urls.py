from django.urls import path
from .views import login_user,register,logout



app_name = 'accounts'
urlpatterns = [
    path('login',login_user,name='login_user'),
    path('register',register,name='register'),
    path('logout',logout,name='logout')
]




