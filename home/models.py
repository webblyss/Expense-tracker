from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.expense_name}'





