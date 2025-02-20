from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import register
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
# Create your views here.

def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            con_password = form.cleaned_data['con_password']

            user = register.objects.create_user(fullname=fullname,username=username,email=email,phone=phone,password=password)
            user.save()
            messages.success(request,'Register successfully')
            return redirect('login')
        
        else:
            messages.success(request,'User is already register')
            return redirect('Register')
    
    else:
        form = RegisterForm()

    context = {
        'form':form
    }
        
    return render(request,'register.html',context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email=email,password=password)
        if user is not None:
            user_login(request,user)
            messages.success(request,'You have login success')
            return redirect('dashboard')
        else:
            messages.success(request,'Wrong email and password')
            return redirect('login')
        
    return render(request,'login.html')

