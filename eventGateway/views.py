from django.shortcuts import render, redirect
from .models import *

def home(request):

    return render(request, 'home.html')

def login(request):

    return render(request, 'log.html')

def register(request):

    return render(request, 'event_reg.html')