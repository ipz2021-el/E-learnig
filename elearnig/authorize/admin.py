from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import elearningUser

# from .forms import ElearningUserCreationForm, ElearningUserChangeForm
from .models import elearningUser

class ElearningUserAdmin(UserAdmin):
    # add_form = ElearningUserCreationForm
    # form = ElearningUserChangeForm
    model = elearningUser
    list_display = ['username', 'first_name', 'last_name', 'index_number']

admin.site.register(elearningUser, ElearningUserAdmin)
