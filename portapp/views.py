from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from portapp.forms import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm
import requests
from pprint import pprint


API_KEY = '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'

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
    
    projects = Project.objects.all().order_by('-id')
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    current_user = request.user
    if request.method == "POST":
        
        form=CommentForm(request.POST,request.FILES)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=current_user
            
            comment.save()
        return HttpResponseRedirect('/contact')
    else:
        form=CommentForm()
    return render (request,'contact.html', {'form': form})

def about(request):
    
    about = About.objects.all().order_by('-id')
    return render(request, 'about.html', {'about': about})

def github(request):
    url = f'https://api.github.com/users/ezekielkibiego/repos={API_KEY}'
    
    user_data = requests.get(url).json()
    pprint(user_data)

    return render(request, 'github.html', {'user_data':user_data})
