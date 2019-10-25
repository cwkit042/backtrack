from django import forms
from .models import Sprint, SprintBacklogItem, Task
from bootstrap_datepicker_plus import DatePickerInput


class AddSprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['number', 'team', 'product','deadline']
        widgets = {
            'deadline': DatePickerInput(), # default date-format %m/%d/%Y will be used
        }

class AddSBIForm(forms.ModelForm):
    class Meta:
        model = SprintBacklogItem
        fields = ['sprint', 'description']


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'effort']
