from django.shortcuts import render, redirect
from .forms import AddProductForm, AddPBIForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, ProductBacklogItem

# Create your views here.

def add_product(request):
    if request.method == "POST":
        add_product_form = AddProductForm(data=request.POST)
        if add_product_form.is_valid():
            new_product = add_product_form.save(commit=False)
            new_product.owner = User.objects.get(id = 1)
            new_product.save()
            return redirect('/')
        else:
            return HttpResponse("The Form is not valid, please post again")
    else:
        add_product_form = AddProductForm()
        context = { 'add_product_form': add_product_form }
        return render(request, 'productbacklog/create.html', context)

def pbi_list(request):
    pbis = ProductBacklogItem.objects.all()
    context = {'pbis': pbis}
    return render(request, 'productbacklog/list.html', context)

def add_pbi(request):
    if request.method == "POST":
        add_pbi_form = AddPBIForm(data=request.POST)
        if add_pbi_form.is_valid():
            new_pbi = add_pbi_form.save(commit=False)
            new_pbi.owner = User.objects.get(id = 1)
            new_pbi.product = Product.objects.get(name = "helloword")
            new_pbi.save()
            return redirect('/productbacklog/')
        else:
            HttpResponse("The Form is not valid, please post again")
    else:
        add_pbi_form = AddPBIForm()
        context = {'add_pbi_form': add_pbi_form}
        return render(request, 'productbacklog/createpbi.html', context)
