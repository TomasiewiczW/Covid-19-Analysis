from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from webmap import models

from .serializers import CountrySerializer
from webmap import models


# Create your views here.
class CountryViewSet(ReadOnlyModelViewSet):
    queryset = models.WorldBorder.objects.all()
    serializer_class = CountrySerializer
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, )


class MainPageView(TemplateView):
    template_name = "webmap/map.html"
