from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from . import views
from eventGateway import views as user_views

urlpatterns = [
    path('', EventsListview.as_view(), name='home'),
    path('event/<int:pk>/', EventsDetileview.as_view(), name='event_detiled_view'),
    path('event/<int:pk>/update/', EventsUpdateview.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventsDeleteview.as_view(), name='event_delete'),
    path('event/new/', EventsCreateview.as_view(), name='event_create'),
    path('events/', views.Events, name='events'),
    path('about_us/', views.AboutUs, name='aboutUs'),
    # Login and Logout
    path('login/', auth_view.LoginView.as_view(template_name='log.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='home.html'), name='logout'),

    path('register/', views.register, name='register'),
    path('userRegister/', user_views.user_register, name='user_register'),
    path('profile/', views.profile, name='profile'),
    path('students/', views.Students, name='students'),

]

