from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepublic'),
    path('eventspublic', views.events, name='eventspublic'),
    path('aboutus', views.aboutus, name='aboutus'),

    # url(r'^home/', views.home),
    # re_path(r'^?/$', views.home),
    # url(r'^about/', views.about),
    # re_path(r'^about?/$', views.about),
]