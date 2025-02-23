from .models import Event, Group
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'duration', 'link', 'description', 'type', 'participants']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'link': forms.URLInput(),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'event', 'students', 'teacher']
        widgets = {
            'students': forms.SelectMultiple(),
            'teacher': forms.Select(),
        }