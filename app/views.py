from django.shortcuts import render
from .forms import RegisterForm
from .models import register
from django.http import HttpResponse
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
            gender = form.cleaned_data['gender']

            user = register.objects.create_user(fullname=fullname,username=username,email=email,phone=phone,password=password,gender=gender)
            user.save()
            return HttpResponse("user register")
    
    else:
        form = RegisterForm()

    context = {
        'form':form
    }
        
    return render(request,'register.html',context)