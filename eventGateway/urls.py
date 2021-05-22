from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from eventGateway import views as user_views

urlpatterns = [
    path('logHome/', views.homead, name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='log.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('user_register/', user_views.user_register, name='user_register'),
    path('profile/', views.profile, name='profile'),

    # url(r'^home/', views.home),
    # re_path(r'^?/$', views.home),
    # url(r'^about/', views.about),
    # re_path(r'^about?/$', views.about),
]