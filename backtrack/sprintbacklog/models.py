from django.db import models
from django.utils import timezone
from userprofile.models import Team, User
from productbacklog.models import Product, ProductBacklogItem

# Create your models here.
NOTSTART = 'N'
INPROGRESS = 'P'
COMPLETE = 'C'
PROGRESS_STATUS = (
    (NOTSTART, 'not start'),
    (INPROGRESS, 'in progress'),
    (COMPLETE, 'complete'),
)

class Sprint (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    progress = models.CharField(
        max_length=1,
        choices=PROGRESS_STATUS,
        default=NOTSTART,
        blank=False,
    )
    deadline = models.DateTimeField()

    def __str__(self):
        return '{product} Sprint {number}'.format(product=self.product, number=self.number)

class SprintBacklogItem (models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    productbacklogitem = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.productbacklogitem.name

class Task (models.Model):
    name = models.CharField(max_length=20, blank=True)
    sprintbacklogitem = models.ForeignKey(SprintBacklogItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    effort = models.IntegerField()
    progress = models.CharField(
        max_length=1,
        choices=PROGRESS_STATUS,
        default=NOTSTART,
        blank=False,
    )

    def __str__(self):
        return self.name
