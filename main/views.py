from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, GroupForm
from django.contrib.auth.decorators import login_required
from .models import Event, EventParticipant
from django.http import JsonResponse

def home(request):
    return render(request, 'base.html')

def calendar(request):
    return render(request, 'calendar.html')

def groupes(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = request.user
            group.save()

            return redirect('groupes')
    else:
        form = GroupForm()

    return render(request, 'groupes.html', {'form': form})



@login_required
def event_list(request):
    pending_events = Event.objects.filter(event_participants__user=request.user, event_participants__status='pending')
    accepted_events = Event.objects.filter(event_participants__user=request.user, event_participants__status='accepted')

    return render(request, 'e/event_list.html', {
        'pending_events': pending_events,
        'accepted_events': accepted_events
    })




@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            form.save_m2m()
            
            for participant in form.cleaned_data['participants']:
                if not EventParticipant.objects.filter(event=event, user=participant).exists():
                    EventParticipant.objects.create(event=event, user=participant, status='pending')

            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'e/event_create.html', {'form': form})



@login_required
def respond_to_event(request, event_id, response):
    event = get_object_or_404(Event, id=event_id)
    participant = EventParticipant.objects.filter(event=event, user=request.user).first()
    
    if response == 'accept':
        participant.status = 'accepted'
    elif response == 'decline':
        participant.status = 'declined'
    participant.save()
    
    return redirect('event_list')



def inbox(request):
    return render(request, 'inbox.html')

def tasks(request):
    return render(request, 'tasks.html')