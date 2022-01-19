from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import elearningUser

from .forms import ElearningUserCreationForm, ElearningUserChangeForm
from .models import elearningUser

class ElearningUserAdmin(UserAdmin):
    add_form = ElearningUserCreationForm
    form = ElearningUserChangeForm
    model = elearningUser
    list_display = ['email', 'username', 'name']

admin.site.register(elearningUser, ElearningUserAdmin)
