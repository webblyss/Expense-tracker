from django.urls import path
from .views import home,delete_expense,update_expense


app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    path('delete_exprense/<int:exprense_id>/',delete_expense,name='delete_exprense'),
    path('update_expense/<int:expense_id>/',update_expense,name='update_expense'),
]
