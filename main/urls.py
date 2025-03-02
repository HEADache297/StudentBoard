from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('calendar/', views.calendar, name='calendar'),
    path('groupes/', views.groupes, name='groupes'),
    path('inbox/', views.inbox, name='inbox'),
    path('tasks/', views.tasks, name='tasks'),

    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:event_id>/<str:response>/', views.respond_to_event, name='respond_to_event'),
]