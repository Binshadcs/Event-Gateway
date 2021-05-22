from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def homead(request):

    return render(request, 'adminhome.html')

def register(request):

    return render(request, 'event_reg.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = UserRegisterForm ()
    return render(request, 'user_register.html',{'form':form})
@login_required
def profile(request):
    return render(request, 'profile.html')
