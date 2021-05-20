from django.shortcuts import render, redirect
from .models import *

def home(request):

    return render(request, 'home.html')

def events(request):

    return render(request, 'events.html')

def aboutus(request):

    return render(request, 'aboutUs.html')
