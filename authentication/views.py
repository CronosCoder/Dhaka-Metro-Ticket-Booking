from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about_us(request):
    return render(request,'about_us/about_us.html')

def contact_us(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        contact = Contact(name = name, email = email, content = content)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_us')
    return render(request,'contact/contact.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Provide correct username and password')
                return redirect('login')
    return render(request,'login/login.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            re_pass = request.POST['re-password']

            if password != re_pass:
                messages.error(request, 'Pasword does not match')
                return redirect('register')
            
            if len(password) < 6 :
                messages.error(request, 'Password should be grater than 5 character')
                return redirect('register')
            
            user = User.objects.create_user(username=username,password=password,email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
            return redirect('login')

    return render(request,'register/register.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def profile_setting(request):
    return render(request,'profile_setting/profile_setting.html')
