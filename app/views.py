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
            messages.success(request,'Register successfully')
        
            try:
                email_subject = "Please Active your Email"
                current_side = get_current_site(request)

                context = {
                    'user':user,
                    'domail':current_side,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':default_token_generator.make_token(user),
                }

                message = render_to_string('register.html',context)
                send_email = EmailMessage(email_subject,message,to=['email'])
                send_email.send()
            except:
                pass

            return redirect(f'login/?command=verification&email='+email)
        
        else:
            message.success(request,'User is already register')
            return redirect('Register')
    
    else:
        form = RegisterForm()

    context = {
        'form':form
    }
        
    return render(request,'register.html',context)

def login(request):
    return render(request,'login.html')

def verification(request,uid64,token):
    try:
        userid = urlsafe_base64_decode(uid64).decode()
        user = register._default_manager.get(id=userid)
        tokens = default_token_generator.check_token(user,token)
    except:
        user = None

    if user is not None and tokens:
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('Register')