from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('please provide email')
        ne = self.normalize_email(email)
        user = self.model(email=ne,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,first_name,last_name,password):
        user=self.create_user(email,first_name,last_name,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects = UserProfileManager()