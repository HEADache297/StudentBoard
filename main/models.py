from django.db import models
from user.models import CustomUser

# Create your models here.

class Event(models.Model):
    EVENT_TYPES = [
        ('exam', 'Exam'),
        ('test', 'Test'),
        ('school', 'School events'),
        ('meeting', 'Parent-teacher conference'),
        ('personal', 'Personal events')
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    event_type = models.CharField(max_length=100, choices=EVENT_TYPES, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    duration = models.DurationField()
    link = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_events')
    participants = models.ManyToManyField(CustomUser, through='EventParticipant', related_name='events')

    def __str__(self):
        return self.title

class EventParticipant(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('pending', 'Pending')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='event_participants')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participants')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.user.username

    
    
class Group(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    students = models.ManyToManyField(CustomUser, related_name='students', limit_choices_to={'is_student': True},)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher', limit_choices_to={'is_teacher': True},)
    event = models.ManyToManyField(Event, related_name='event', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} ({self.teacher}) {self.students.all()}"
    
    def __repr__(self):
        return f"{self.name} {self.description} ({self.teacher}) {self.students.all()}"
    

