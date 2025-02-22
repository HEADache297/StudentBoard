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
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({'id': 'signup_email'})
    #     self.fields['password1'].widget.attrs.update({'id': 'signup_password1'})
    #     self.fields['password2'].widget.attrs.update({'id': 'signup_password2'})

class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Email'}), label='Email')    
    password = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'id': 'login_email'})
    #     self.fields['password'].widget.attrs.update({'id': 'login_password'})

class studentCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=Input(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Name'}))
    surname = forms.CharField(max_length=255, widget=Input(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Surname'}))
    email = forms.CharField(max_length=255, widget=EmailInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=255, widget=PasswordInput(attrs={'class': 'm-3 h-12 rounded-lg p-2 bg-secondary text-dark', 'placeholder': 'Check password'}))
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('parents', 'Parents')], widget=forms.Select(attrs={'class': 'p-2 rounded-lg bg-accent-200 text-dark'}))

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'password1', 'password2', 'user_type']