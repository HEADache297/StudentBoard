from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import Input, PasswordInput, EmailInput
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255, widget=Input(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Name'}))
    surname = forms.CharField(max_length=255, widget=Input(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Surname'}))
    email = forms.CharField(max_length=255, widget=EmailInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Check password'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'surname', 'password1', 'password2')

class CustomUserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Email'}), label='Email')    
    password = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
