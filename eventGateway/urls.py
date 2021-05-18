from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    # url(r'^home/', views.home),
    # re_path(r'^?/$', views.home),
    # url(r'^about/', views.about),
    # re_path(r'^about?/$', views.about),
]