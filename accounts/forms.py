from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AddUser


class AddUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AddUser
        fields = ('username', 'email', 'telefon', 'profile_photo')
        
class AddUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = AddUser
        fields = ('username', 'email', 'telefon', 'profile_photo')