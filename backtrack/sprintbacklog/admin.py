from django.contrib import admin
from .models import Sprint, SprintBacklogItem
# Register your models here.

admin.site.register(Sprint)
admin.site.register(SprintBacklogItem)
