from .models import Event, Group, CustomUser
from django import forms

class EventForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), required=False)

    class Meta:
        model = Event
        fields = ['title', 'date', 'duration', 'link', 'description', 'event_type', 'participants']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'link': forms.URLInput(),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'students', 'description']
        widgets = {
            'students': forms.SelectMultiple(),
        }