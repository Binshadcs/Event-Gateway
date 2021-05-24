from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'events': Events.object.all()
    }
    return render(request, 'home.html', context)

class EventsListview(ListView):
    model = Events
    template_name = 'home.html'
    # <app>/<model>_<viewtype>.html

    context_object_name = 'events'
    ordering = ['date']


class EventsDetileview(DetailView):
    model = Events
    template_name = 'events_detail.html'


class EventsCreateview(LoginRequiredMixin, CreateView):
    model = Events
    template_name = 'event_form.html'
    fields = [
        'title',
        'description',
        'date',
        'time',
        'venue',
        'max_participants',
        'banner'
    ]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventsUpdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    template_name = 'event_form.html'
    fields = [
        'title',
        'description',
        'date',
        'time',
        'venue',
        'max_participants',
        'banner'
    ]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False


class EventsDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    success_url = '/'
    template_name = 'event_delete.html'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False



def AboutUs(request):
    return render(request, 'aboutUs.html')


def Events(request):
    return render(request, 'events.html')


@login_required
def register(request):

    return render(request, 'event_reg.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm ()
    return render(request, 'user_register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'profile.html')


def Students(request):

    return render(request, 'students.html')






