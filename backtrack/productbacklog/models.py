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

    NOTSTART = 'N'
    INPROGRESS = 'P'
    COMPLETE = 'C'
    PROGRESS_STATUS = (
        (NOTSTART, 'not start'),
        (INPROGRESS, 'in progress'),
        (COMPLETE, 'complete'),
    )

    progress = models.CharField(
        max_length=1,
        choices=PROGRESS_STATUS,
        default=NOTSTART,
        blank=False,
    )

    storypoint = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.name

#class ProductBacklogItemOrder (models.Model):
#    productbacklogitem = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE, null=True)
#    headpbi = models.ForeignKey(ProductBacklogItem, related_name='headpbi' ,on_delete=models.SET_NULL, null=True)
#    tailpbi = models.ForeignKey(ProductBacklogItem, related_name='tailpbi', on_delete=models.SET_NULL, null=True)
#    def __str__(self):
#        return self.productbacklogitem.name
