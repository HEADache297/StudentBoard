from django.shortcuts import render, redirect
from .forms import EventForm, GroupForm

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def groupes(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupes')
    else:
        form = GroupForm()

    return render(request, 'groupes.html', {'form': form})

def inbox(request):
    return render(request, 'inbox.html')

def tasks(request):
    return render(request, 'tasks.html')