from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from portapp.forms import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
   
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authanticated' ' Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid login')
    else:
        form=LoginForm()
    return render(request,'account/login.html', {'form': form})

def projects(request):
    current_user = request.user
    projects = Project.objects.all().order_by('-id')
    return render(request, 'index.html', {'projects': projects,'current_user':current_user})