from django.db import models
from django.utils import timezone
from userprofile.models import Team, User
from productbacklog.models import Product, ProductBacklogItem

# Create your models here.

class Sprint (models.Model):
    project = models.ForeignKey(Product, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    progress = models.CharField(max_length=10)
    deadline = models.DateTimeField()

class SprintBacklogItem (models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    productbacklogitem = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Task (models.Model):
    sprintbacklogitem = models.ForeignKey(SprintBacklogItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    effort = models.IntegerField()
