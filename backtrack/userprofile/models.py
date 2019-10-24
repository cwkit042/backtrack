from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    type = models.CharField(max_length=10, default='developer')
    
    def __str__(self):
        return 'user {}'.format(self.user.name)
        
class Team(models.Model):
    name = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(default=timezone.now)

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
