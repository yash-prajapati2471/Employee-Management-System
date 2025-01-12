from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    con_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password'}))

    class Meta:
        model = register
        fields = ['fullname','username','email','phone','gender','password']


    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get('password')
        con_password = cleaned_data.get('con_password')

        if password != con_password:
            raise forms.ValidationError("Password and Confirm Password does not match")
        
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['fullname'].widget.attrs['placeholder'] = "Enter your fullname"        
        self.fields['username'].widget.attrs['placeholder'] = "Enter your username"        
        self.fields['email'].widget.attrs['placeholder'] = "Enter your email"        
        self.fields['phone'].widget.attrs['placeholder'] = "Enter your phone number"
               
