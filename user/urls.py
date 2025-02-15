from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # path('sign_up/', views.sign_up, name='register'),
    path('authorisation/', views.authorisation, name='authorisation'),
    path('addStudent/', views.addStudent, name='add_student'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]