from django.contrib import admin
from django.urls import path
from criminalDetector import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sbp', views.sbp, name='sbp'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),

]
