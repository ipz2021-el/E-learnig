from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import ElearningUserManager


class ElearningUser(AbstractUser):
    TYPES = [('STUDENT','student'),('TEACHER','teacher'),('ADMIN','admin')]
    username = models.CharField(unique=True,max_length=50,null=True)
    email = models.EmailField(_('email address'), unique=True)
    index_number = models.IntegerField(blank=True, null=True, unique=True)
    street_address = models.CharField(blank=True,null=True,max_length=150)
    zip_code = models.CharField(blank=True,null=True,max_length=6)
    city = models.CharField(blank=True,null=True,max_length=150)
    phone_number = models.IntegerField(blank=True,null=True)
    department = models.CharField(blank=True,null=True,max_length=150)
    university = models.CharField(blank=True,null=True,max_length=150)
    type = models.CharField(choices=TYPES,max_length=7,default='STUDENT')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ElearningUserManager()
    

    def __str__(self):
        return self.email
