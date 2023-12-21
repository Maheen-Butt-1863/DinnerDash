# forms.py in yourapp
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from dinnerApp.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['display_name', 'email']


class CustomUserChangeForm(UserChangeForm):
    pass