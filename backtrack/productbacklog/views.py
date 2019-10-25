from django.shortcuts import render, redirect
from django.db.models import F
from .forms import AddProductForm, AddPBIForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, ProductBacklogItem, ProductBacklogItemOrder

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

def pbi_current_list(request):
    pbis = ProductBacklogItem.objects.filter(progress = 'N')
    context = {'pbis': pbis}
    return render(request, 'productbacklog/currentlist.html', context)

def pbi_list(request):
    pbis = ProductBacklogItem.objects.all()
    context = {'pbis': pbis}
    return render(request, 'productbacklog/list.html', context)

def order_list(request):
    # pbis = ProductBacklogItemOrder.objects.filter(productbacklogitem__product__name = 'helloword')
    # order_list = []
    # for pbi in pbis:
    #     if pbi.headpbi == None:
    #         order_list.append(pbi)
    #         while True:
    #             if pbi.tailpbi == None:
    #                 break
    #             pbi = ProductBacklogItemOrder.objects.get(productbacklogitem=pbi.tailpbi)
    #             order_list.append(pbi)
    order_list = ProductBacklogItem.objects.filter(order__gt=0, product__name='helloword').order_by('order')
    context = {'pbis': order_list}
    return render(request, 'productbacklog/orderlist.html', context)

def add_pbi(request):
    if request.method == "POST":
        add_pbi_form = AddPBIForm(data=request.POST)
        if add_pbi_form.is_valid():
            new_pbi = add_pbi_form.save(commit=False)
            new_pbi.owner = User.objects.get(id = 1)
            new_pbi.product = Product.objects.get(name = "helloword")
            new_pbi.save()
            target_pbi = request.POST.get('follow')
            order_list = ProductBacklogItem.objects.filter(order__gt=0, product__name='helloword')
            if not order_list.exists():
                new_pbi.order = 1
                new_pbi.save()
            elif target_pbi =='':
                order_list = ProductBacklogItem.objects.filter(order__gt=0, product__name='helloword')
                order_list.update(order=F('order')+1)
                new_pbi.order = 1
                new_pbi.save()
            else:
                target_pbi_object = ProductBacklogItem.objects.get(id=target_pbi)
                order_list = ProductBacklogItem.objects.filter(order__gt=target_pbi_object.order,product__name='helloword')
                order_list.update(order=F('order')+1)
                new_pbi.order = target_pbi_object.order+1
                new_pbi.save()
            return redirect('/productbacklog/')
            #order_list = ProductBacklogItemOrder.objects.filter(productbacklogitem__product=new_pbi.product)
            #print(order_list)
            # target_pbi = request.POST.get('follow')
            # order_list = ProductBacklogItem.objects.filter(order>0, product=target_pbi.product)
            #if len(order_list)==0:
                # new_order = ProductBacklogItemOrder(
                #     productbacklogitem = new_pbi,
                #     headpbi = None,
                #     tailpbi = None,
                # )
                # new_order.save()
            #elif target_pbi == '':
                #head = ProductBacklogItemOrder.objects.filter(headpbi = None, productbacklogitem__product = new_pbi.product)[0]
                # new_order = ProductBacklogItemOrder(
                #     productbacklogitem = new_pbi,
                #     headpbi = None,
                #     tailpbi = head.productbacklogitem,
                # )
                # new_order.save()
                # head.headpbi = new_order.productbacklogitem
                # head.save()
            #else:
                #head = ProductBacklogItemOrder.objects.get(productbacklogitem = target_pbi)
                # try:
                #     tail = ProductBacklogItemOrder.objects.get(headpbi = target_pbi)
                # except ProductBacklogItemOrder.DoesNotExist:
                #     tail = None
                # if tail != None:
                #     new_order = ProductBacklogItemOrder(
                #         productbacklogitem = new_pbi,
                #         headpbi = head.productbacklogitem,
                #         tailpbi = head.tailpbi,
                #     )
                #     head.tailpbi = new_order.productbacklogitem
                #     tail.headpbi = new_order.productbacklogitem
                #     new_order.save()
                #     head.save()
                #     tail.save()
                # else:
                #     new_order = ProductBacklogItemOrder(
                #         productbacklogitem = new_pbi,
                #         headpbi = head.productbacklogitem,
                #         tailpbi = None,
                #     )
                #     head.tailpbi = new_order.productbacklogitem
                #     new_order.save()
                #     head.save()
                #     return redirect('/productbacklog/')
        else:
            HttpResponse("The Form is not valid, please post again")
    else:
        add_pbi_form = AddPBIForm()
        pbi_list = ProductBacklogItem.objects.filter(order__gt=0).filter(product = Product.objects.get(name = "helloword").id).order_by('order')
        context = {'add_pbi_form': add_pbi_form, 'pbi_list':pbi_list}
        return render(request, 'productbacklog/createpbi.html', context)
def switch_pbi(request):
    if request.method == "POST":
        #print(request.POST.getlist("switch", None))
        switch_list= request.POST.getlist("switch")
        #print(switch_list[0])
        if len(switch_list) >= 2:
            head = ProductBacklogItem.objects.get(id=switch_list[0])
            tail = ProductBacklogItem.objects.get(id=switch_list[1])
            temp = head.order
            head.order = tail.order
            tail.order = temp
            head.save()
            tail.save()
        # head = ProductBacklogItemOrder.objects.get(productbacklogitem=switch_list[0])
        # tail = ProductBacklogItemOrder.objects.get(productbacklogitem=switch_list[1])
        # temp = tail
        # upper1 = ProductBacklogItemOrder.objects.get(headpbi=switch_list[0])
        # lower1 = ProductBacklogItemOrder.objects.get(tailpbi=switch_list[1])
        # upper1.headpbi = ProductBacklogItem.objects.get(id=switch_list[1])
        # lower1.tailpbi = ProductBacklogItem.objects.get(id=switch_list[0])
        #
        #
        # tail.headpbi = head.headpbi
        # tail.tailpbi = head.tailpbi
        # head.headpbi = temp.headpbi
        # head.tailpbi = temp.tailpbi
        #
        # if ProductBacklogItemOrder.objects.get(productbacklogitem=switch_list[0]).headpbi != None:
        #     upper = ProductBacklogItemOrder.objects.get(tailpbi=switch_list[0])
        #     upper.tailpbi = ProductBacklogItem.objects.get(id=switch_list[1])
        #     if ProductBacklogItemOrder.objects.get(productbacklogitem=switch_list[1]).tailpbi != None:
        #         lower = ProductBacklogItemOrder.objects.get(headpbi=switch_list[1])
        #         lower.headpbi = ProductBacklogItem.objects.get(id=switch_list[0])
        #         lower.save()
        #     upper.save()
        # elif ProductBacklogItemOrder.objects.get(productbacklogitem=switch_list[1]).tailpbi != None:
        #     lower = ProductBacklogItemOrder.objects.get(headpbi=switch_list[1])
        #     lower.headpbi = ProductBacklogItem.objects.get(id=switch_list[0])
        #     lower.save()
        # upper1.save()
        # lower1.save()
        # head.save()
        # tail.save()


    return redirect('/productbacklog/orderlist')
