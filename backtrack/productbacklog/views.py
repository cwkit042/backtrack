from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .forms import AddProductForm, AddPBIForm, ProductBacklogForm
from userprofile.models import Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, ProductBacklogItem

# Create your views here.

@login_required(login_url='/login')
def add_product(request):
    if request.user.profile.type == 'PO':
        if request.method == "POST":
            add_product_form = AddProductForm(data=request.POST)
            if add_product_form.is_valid():
                new_product = add_product_form.save(commit=False)
                new_product.owner = User.objects.get(id = request.user.id)
                new_product.save()
                return redirect('/')
            else:
                return HttpResponse("The Form is not valid, please post again")
        else:
            add_product_form = AddProductForm()
            context = { 'add_product_form': add_product_form }
            return render(request, 'productbacklog/create.html', context)
    else:
        return HttpResponse("You are not Product Owner!")

@login_required(login_url='/login')
def pbi_current_list(request):
    pbis = ProductBacklogItem.objects.filter(progress = 'N')
    context = {'pbis': pbis}
    return render(request, 'productbacklog/currentlist.html', context)
    
@login_required(login_url='/login')
def homepage(request):
    if Profile.objects.filter(user_id=request.user.id).exists():
        profile = Profile.objects.get(user_id=request.user)
    else:
        profile = Profile.objects.create(user=request.user)
    if profile.type == 'PO':
        return redirect('/productbacklog/orderlist/')
    elif profile.type == 'DV':
        return redirect('/sprintbacklog/')
    else:
        return HttpResponse("Your User is not either Developer or Product Owner")

@login_required(login_url='/login')
def pbi_list(request):
    pbis = ProductBacklogItem.objects.all()
    print(request.user)
    if Profile.objects.filter(user_id=request.user.id).exists():
        profile = Profile.objects.get(user_id=request.user)
    else:
        profile = Profile.objects.create(user=request.user)
    #PO DV
    print(profile.type)
    context = {'pbis': pbis}
    return render(request, 'productbacklog/list.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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
        
@login_required(login_url='/login')
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
    
@login_required(login_url='/login')
def delete_pbi(request):
    if request.method == "POST":
        pbiId = request.POST.get('id');
        productA = Product.objects.get(productbacklogitem = pbiId)
        owner = productA.owner
        pbi = ProductBacklogItem.objects.get(id = pbiId)
        print(owner)
        if owner == request.user:
            pbiOrder = pbi.order;
            print(pbiOrder);
            pbis = ProductBacklogItem.objects.filter(product = productA)
            for pbiA in pbis:
                if pbiA.order > pbiOrder:
                    pbiA.order -= 1
                    pbiA.save()
            pbi.delete()
            return redirect('/productbacklog/orderlist')
        else:
            return HttpResponse("You are not the product owner of this Product")
    else:
        return HttpResponse("ONLY POST ALLOWED")

def modify_pbi(request):
    if request.method == "POST":
        pbiId = request.POST.get('id');
        productA = Product.objects.get(productbacklogitem = pbiId)
        owner = productA.owner
        pbi = ProductBacklogItem.objects.get(id = pbiId)
        print(owner)
        if owner == request.user:
            product_form = ProductBacklogForm(data=request.POST)
            if product_form.is_valid():
                pbi_cd = product_form.cleaned_data
                pbi.description = pbi_cd['description']
                pbi.name = pbi_cd['name']
                pbi.storypoint = pbi_cd['storypoint']
                pbi.save()
                return redirect('/productbacklog/orderlist')
            else:
                return HttpResponse("invalid form")
        else:
            return HttpResponse("You are not the product owner of this Product")
    else:
        return HttpResponse("ONLY POST ALLOWED")