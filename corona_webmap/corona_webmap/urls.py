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
from django.urls import path, include
from webmap import views
from djgeojson.views import GeoJSONLayerView

from webmap.models import WorldBorder

urlpatterns = [
    path('', views.WebmapTemplateView.as_view()),
    path('admin/', admin.site.urls),
    path('data.geojson', GeoJSONLayerView.as_view(model=WorldBorder, properties=('name', 'population', 'area', 'location')), name='data')
]
