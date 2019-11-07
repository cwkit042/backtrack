from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("/productbacklog/")
            else:
                user_login_form = UserLoginForm()
                context = {'form':user_login_form, 'fail':True}
                return render(request, "userprofile/login.html", context)
        else:
            return HttpResponse("invalid username or password")
    elif request.method == "GET":
        if request.user.is_authenticated:
            redirect('/');
        else:
            user_login_form = UserLoginForm()
            context = {'form':user_login_form, 'fail':False}
            return render(request, 'userprofile/login.html', context)
        
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('/login/')


def user_register(request):
    if request.user.is_authenticated:
            redirect('/');
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        print(user_register_form)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            if(user_register_form.cleaned_data['type'] != "DV"):
                profile.type = user_register_form.cleaned_data['type']
                profile.save()
            login(request, new_user)
            return redirect('/')
        else:
            return HttpResponse("invalid register form")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context =  {'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("ONLY POST OR GET")