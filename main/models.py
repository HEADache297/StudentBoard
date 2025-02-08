from django.db import models
from user.models import CustomUser

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    duration = models.IntegerField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    type = models.CharField(max_length=100, null=False, blank=False)
    participants = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return self.name
    
    
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
    

