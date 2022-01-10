from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from portapp.forms import *


def index(request):
   
    return render(request, 'index.html')