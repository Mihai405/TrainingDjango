from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**other_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        email=self.normalize_email(email)
        user=self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password=None,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)



class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    username=None

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    def __str__(self):
        return self.first_name