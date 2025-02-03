from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'surname', 'password1', 'password2')

class CustomUserLoginForm(AuthenticationForm):
     class Meta:
        model = CustomUser
        fields = ('email', 'password')
