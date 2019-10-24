from django.shortcuts import render
from .forms import AddSprintForm, AddSBIForm, AddTaskForm
from django.http import HttpResponse
from djangp.contrib.auth.models import User
from .models import Sprint, SprintBacklogItem, Task

def add_sprint(request):
    if request.method == "POST":
        add_sprint_form = AddSprintForm(data=request.POST)
        
