from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['name']
    

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())
    location = models.TextField(max_length=100)
    duration = models.IntegerField(default=1)
    desc = models.TextField()
    limit = models.IntegerField(default=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.date}"
    
    class Meta:
        ordering = ['created_at']
    
    
class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participant')

    def __str__(self):
        return f"{self.event.name}: {self.member.first_name} {self.member.last_name}"
