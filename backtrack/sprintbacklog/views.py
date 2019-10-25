from django.shortcuts import render, redirect
from .forms import AddSprintForm, AddSBIForm, AddTaskForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Sprint, SprintBacklogItem, Task
from productbacklog.models import Product, ProductBacklogItem
from django.views import generic
from bootstrap_datepicker_plus import DatePickerInput

def sprint_list(request):
    sprints = Sprint.objects.all()
    context = {'sprints': sprints}
    return render(request, 'sprintbacklog/list.html',context)

def sbi_list(request, id):
    target_sprint = Sprint.objects.get(id=id)
    sbi_list = SprintBacklogItem.objects.filter(sprint=target_sprint.id)
    sbi_id_list = []
    for sbi in sbi_list:
        sbi_id_list.append(sbi.id)
    print(sbi_id_list)
    task_list = Task.objects.filter(sprintbacklogitem__in=sbi_id_list)
    for task in task_list:
        print(task)
    context = {'sbi_list': sbi_list, 'task_list': task_list, 'sprint_number': target_sprint.number}
    return render(request, 'sprintbacklog/sbilist.html',context)

class CreateSprintView(generic.edit.CreateView):
    model = Sprint
    form_class = AddSprintForm
    template_name = 'sprintbacklog/createsprintview.html'
    success_url="/sprintbacklog/"
    def get_form(self):
         form = super().get_form()
         form.fields['deadline'].widget = DatePickerInput()
         return form

def add_sbi(request, id):
    target_pbi = ProductBacklogItem.objects.get(id=id)
    if request.method == "POST":
        add_sbi_form = AddSBIForm(data=request.POST)
        if add_sbi_form.is_valid():
            new_sbi = add_sbi_form.save(commit=False)
            new_sbi.productbacklogitem = target_pbi
            new_sbi.save()
            target_pbi.progress = 'P'
            target_pbi.save()
            return redirect('/productbacklog/pbicurrentlist')
        else:
            return HttpResponse("The Form is not valid, please post again")
    else:
        add_sbi_form = AddSBIForm()
        sprint_list = Sprint.objects.all()
        context = {'add_sbi_form': add_sbi_form,'sprint_list': sprint_list, 'target_pbi':target_pbi}
        return render(request, 'sprintbacklog/createsbi.html', context)

def add_task(request, id):
    target_sbi = SprintBacklogItem.objects.get(id=id)
    if request.method == "POST":
        add_task_form = AddTaskForm(data=request.POST)
        if add_task_form.is_valid():
            new_task = add_task_form.save(commit=False)
            new_task.sprintbacklogitem = target_sbi
            new_task.save()
            return redirect('/sprintbacklog/sbilist/'+str(target_sbi.sprint.number)+'/')
        else:
            return HttpResponse("The Form is not valid, please post again")
    else:
        add_task_form = AddTaskForm()
        context = {'add_task_form': add_task_form, 'target_sbi':target_sbi}
        return render(request, 'sprintbacklog/createtask.html', context)
