from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    DEVELOPER = 'DV'
    PRODUCTOWNER = 'PO'
    USER_TYPE = (
        (DEVELOPER, 'developer'),
        (PRODUCTOWNER , 'product owner'),
    )

    type = models.CharField(
        max_length=2,
        choices = USER_TYPE,
        default=DEVELOPER,
    )

    def __str__(self):
        return 'user {}'.format(self.user.name)

class Team(models.Model):
    name = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
