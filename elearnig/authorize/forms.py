from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import elearningUser

class ElearningUserCreationForm(UserCreationForm):  

    class Meta:
        model = elearningUser
        fields = ('first_name', 'last_name', 'index_number','type')

class ElearningUserChangeForm(UserChangeForm):

    class Meta:
        model = elearningUser
        fields = ('first_name', 'last_name', 'index_number','type')