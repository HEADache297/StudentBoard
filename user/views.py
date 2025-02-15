from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
# Create your views here.

def authorisation(request):
    login_form = CustomUserLoginForm()
    signup_form = CustomUserRegistrationForm() 

    if request.method == 'POST':
        if 'login' in request.POST: 
            print(request.POST)
            login_form = CustomUserLoginForm(request, data=request.POST)

            if login_form.is_valid():

                print('EMAIL EMAIL',login_form.cleaned_data.get('username'))
                print('PAASSWORD PASSWORD',login_form.cleaned_data.get('password'))

                user = authenticate(
                    username=login_form.cleaned_data.get('username'),
                    password=login_form.cleaned_data.get('password')
                )
                print(user,'user user')
                if user is not None:
                    print(user)
                    auth_login(request, user)
                    return redirect('/home')  
                else:
                    messages.error(request, 'Incorrect login details')
                    print(login_form.errors)
            else:
                messages.error(request, 'Login error')
                
        
        else: 
            print('sign_form')

            signup_form = CustomUserRegistrationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                return redirect('/home')  
            else:
                messages.error(request, 'Error during registration')
            
    else:
        login_form = CustomUserLoginForm()
        signup_form = CustomUserRegistrationForm()

    return render(request, 'registration/authorisation.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })



def logout(request):
    from django.contrib.auth import logout
    logout(request)

    return redirect('homepage')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def addStudent(request):
    return render(request, 'addStudent.html')
