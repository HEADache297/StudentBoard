from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
from django.contrib.auth import login as auth_login, authenticate
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/') 
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password')) 

            if user is not None:
                auth_login(request, user)
                return redirect('/') 

    else:
        form = CustomUserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    from django.contrib.auth import logout
    logout(request)

    return redirect('homepage')