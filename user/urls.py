from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]