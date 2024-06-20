from django.urls import path
from django.contrib import admin
from .views import indexView

app_name = 'app_services'

urlpatterns = [
    path('', indexView.as_view(), name='services')
]
