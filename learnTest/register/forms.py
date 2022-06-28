from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField() #adding email form

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] #fields to show on the site
