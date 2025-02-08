from django.shortcuts import render

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def groupes(request):
    return render(request, 'groupes.html')

def inbox(request):
    return render(request, 'inbox.html')

def tasks(request):
    return render(request, 'tasks.html')