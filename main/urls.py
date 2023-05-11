from django.urls import path
from django.contrib import admin
from .import views



urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('index', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('create-post', views.create_post, name='create_post'),    
    path('CV', views.CV, name='CV'),    
]
