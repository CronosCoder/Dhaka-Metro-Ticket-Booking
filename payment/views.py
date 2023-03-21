from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def payment_page(request):
    return render(request,'payment/payment.html')

@login_required(login_url='login')
def success_page(request):
    user = request.user
    name = user.first_name+" "+user.last_name
    return render(request,'success/success.html',{"name":name})
