from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.contrib import messages
# Create your views here.



@login_required(login_url='accounts/login')
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    price_list = []
    
    if request.method == 'POST':
        expense_name = request.POST['expense-name']
        amount = request.POST['amount']
        
        new_expense = Expense.objects.create(expense_name=expense_name,amount=amount,user=request.user)
        new_expense.save()
        messages.info(request,'expense created successfully')
        return redirect('/')
    
    
    # CALCULATE PRICE OR AMOUNT
    for item in expenses:
        print(item.amount)
        price_list.append(int(item.amount)) 
    
    total_price = sum(price_list)
    
    
    context = {
        'expenses': expenses,
        'total_price':total_price
    }
    
    
    
    return render(request,'index.html',context)





def delete_exprense(request,exprense_id):
    expense = get_object_or_404(Expense, id=exprense_id)
    expense.delete()
    print('exprense deleted successfully')
    return redirect(request.META.get('HTTP_REFERER'))
    
    
    
    
    
    
    
    
    
    
    





 


