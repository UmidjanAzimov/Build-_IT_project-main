import imp
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AddUserCreationForm, AddUserChangeForm
from .models import AddUser

# Register your models here.

class AddUserAdmin(UserAdmin):
    add_form = AddUserCreationForm
    form = AddUserChangeForm
    model = AddUser
    list_display = ['username', 'email', 'telefon', 'profile_photo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('telefon', 'profile_photo',)}),
    )

admin.site.register(AddUser, AddUserAdmin)