from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from userprofile.models import Team

# Create your models here.
class Product (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    progress = models.CharField(max_length=20, default="not_started")
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductBacklogItem (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
#    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    progress = models.CharField(max_length=20, default="not_started")
    storypoint = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
