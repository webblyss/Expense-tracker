from django.urls import path
from .views import home,delete_exprense


app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    path('delete_exprense/<int:exprense_id>/',delete_exprense,name='delete_exprense'),
]
