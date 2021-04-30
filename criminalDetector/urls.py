from django.contrib import admin
from django.urls import path
from criminalDetector import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
