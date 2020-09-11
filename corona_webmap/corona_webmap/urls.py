"""corona_webmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from webmap import views
from rest_framework.routers import DefaultRouter

from webmap.models import WorldBorder

api_router = DefaultRouter()
api_router.register(r'^v1/cases.geojson', views.CountryViewSet, basename='api')
app_name = "webmap"

urlpatterns = [
    path('api/', include(api_router.urls), name='data'),
    path('', views.MainPageView.as_view()),

]
