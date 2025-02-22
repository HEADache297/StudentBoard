from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, CustomUserLoginForm, studentCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.http import HttpResponse
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
    if not request.user.is_teacher:
        return HttpResponse('Access denied', status=403)

    if request.method == 'POST':
        form = studentCreationForm(request.POST)
        print('form', form)
        if form.is_valid():
            user = form.save(commit=False)
            print('user', user)
            user_type = form.cleaned_data['user_type']
            print(user_type)

            if user_type == 'student':
                user.is_student = True
                user.is_teacher = False
                user.is_parents = False

            elif user_type == 'teacher':
                user.is_student = False
                user.is_teacher = True
                user.is_parents = False

            elif user_type == 'parents':
                user.is_student = False
                user.is_teacher = False
                user.is_parents = True

            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, f'{user_type.capitalize()} successfully added!')
            return redirect('add_student')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = studentCreationForm()

    return render(request, 'addStudent.html', {'form': form})
