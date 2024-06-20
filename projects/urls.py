from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app_projects'

urlpatterns = [
    path('page-<int:page>/', views.indexView.as_view(), name='projects_page'),
    path('category-<str:category>/',
         views.indexView.as_view(), name='projects_category'),
    path('', views.indexView.as_view(), name='projects'),
    path('detail-<slug:slug>', views.detailProjectView.as_view(),
         name='detail_ProjectView'),
    path('report_project/<slug:proyek_slug>/',
         views.report_project, name='report_project'),
]
