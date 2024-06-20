"""
URL configuration for PORTFOLIO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from projects.views import ProyekViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('proyek', ProyekViewSet)

app_name = 'app_home'
urlpatterns = [
    path('', views.index),
    path('about/', include('about.urls')),
    path('education/', include('education.urls')),
    path('skill/', include('skill.urls')),
    path('projects/', include('projects.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path("admin/", admin.site.urls),
    # path('API/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
