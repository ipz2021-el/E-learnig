from operator import mod
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class elearningUser(AbstractUser):
    TYPES = [('STUDENT','student'),('TEACHER','teacher')]
    username = models.CharField(blank=True, null=True, max_length=50)
    index_number = models.IntegerField(blank=True, null=True, unique=True)
    first_name = models.CharField(blank=True,max_length=150)
    last_name = models.CharField(blank=True,max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    street_address = models.CharField(blank=True,null=True,max_length=150)
    zip_code = models.CharField(blank=True,null=True,max_length=6)
    city = models.CharField(blank=True,null=True,max_length=150)
    phone_number = models.IntegerField(blank=True,null=True)
    department = models.CharField(blank=True,null=True,max_length=150)
    university = models.CharField(blank=True,null=True,max_length=150)
    type = models.CharField(choices=TYPES,max_length=7)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'index_number','type']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
