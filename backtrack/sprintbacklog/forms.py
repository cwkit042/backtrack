from django import forms
from .models import Sprint, SprintBacklogItem, Task

class AddSprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields('deadline', 'team', 'project')

class AddSBIForm(forms.ModelForm):
    class Meta:
        model = SprintBacklogItem
        fields('sprint', 'productbacklogitem', 'description')

class AddTaskForm(forms.ModelForm):
    class Meta:
        fields('sprintbacklogitem', 'description', 'owner', 'effort')
