from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('groupes/', views.groupes, name='groupes'),
    path('inbox/', views.inbox, name='inbox'),
    path('tasks/', views.tasks, name='tasks'),
]