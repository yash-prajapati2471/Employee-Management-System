from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,fullname,username,email,phone,gender,password=None):
        user = self.model(
            email = self.normalize_email(email),
            fullname=fullname,
            username=username,
            phone=phone,
            gender=gender
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,fullname,username,email,phone,gender,password):
        user = self.create_user(
            email = self.normalize_email(email),
            fullname=fullname,
            username=username,
            phone=phone,
            gender=gender,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self.db)
        return user

class register(AbstractBaseUser):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    GENDER_CHOICES = [('male','Male'),('female','Female'),('prefer_not_to_say','Prefer not to say')]
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='prefer_not_to_say')

    created_at = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname','username','phone','gender']

    def __str__(self):
        return self.email
    
    def has_module_perms(self,add_label):
        return True
    
    def has_perm(self,perm,obj=None):
        return self.is_admin