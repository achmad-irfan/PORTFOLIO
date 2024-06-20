from django.urls import path,include
from django.contrib import admin
from . import views

app_name='app_contact'
urlpatterns=[
    path('', views.index, name='contact'),
]