from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.db.models import Max, Sum
from webmap import models

from .serializers import CountrySerializer, SelectedGeometrySerializer
from webmap import models

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CountryViewSet(ReadOnlyModelViewSet):
    queryset = models.WorldBorder.objects.all()
    serializer_class = CountrySerializer
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, )


class SelectedGeometryViewSet(ReadOnlyModelViewSet):
    serializer_class = SelectedGeometrySerializer
    bbox_filter_field = 'mpoly'
    filter_backends = (InBBoxFilter, )

    def get_queryset(self, **kwargs):
        queryset = models.WorldBorder.objects.filter(name=self.kwargs['country_name']).only('mpoly')
        return queryset


class MainPageView(TemplateView):
    confirmed_total = models.Confirmed.objects.values('country_id__name').annotate(Max('total')).aggregate(Sum('total__max'))['total__max__sum']
    template_name = "webmap/map.html"

    def get_context_data(self, **context):
        context['confirmed_total'] = self.confirmed_total
        return context


@api_view(['GET'])
def dataLoad(request, pk):
    # main class
    try:
        country = models.WorldBorder.objects.get(name=pk)
    except models.WorldBorder.DoesNotExist:
        content = {pk:'No such country'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    # supplemental data
    try:
        gdp = models.GDP.objects.get(country_id=country.name)
    except models.GDP.DoesNotExist:
        gdp = models.GDP(rank=None, gdpPerCapita=None)

    try:
        smoking = models.Smoking.objects.get(country_id=country.name)
    except models.Smoking.DoesNotExist:
        smoking = models.Smoking(male=None, female=None, total=None)

    try:
        healthcare = models.Healthcare.objects.get(country_id=country.name)
    except models.Healthcare.DoesNotExist:
        healthcare = models.Healthcare(rank=None, score=None)

    try:
        bloodtype = models.Bloodtype.objects.get(country_id=country.name)
    except models.Bloodtype.DoesNotExist:
        bloodtype = models.Bloodtype(Ominus=None, Oplus=None, Aminus=None, Bminus=None, Bplus=None, ABminus =None, ABplus=None)

    # covid data
    try:
        confirmed = models.Confirmed.objects.filter(country_id=country.name).latest('date')
    except models.Confirmed.DoesNotExist:
        confirmed = models.Confirmed(date=None, total=None)

    try:
        recovered = models.Recovered.objects.filter(country_id=country.name).latest('date')
    except models.Recovered.DoesNotExist:
        recovered = models.Recovered(date=None, total=None)

    try:
        deaths = models.Deaths.objects.filter(country_id=country.name).latest('date')
    except models.Deaths.DoesNotExist:
        deaths = models.Deaths(date=None, total=None)

    all_data = {
        'Country':
            {
                'name': country.name,
                'area': country.area,
                'pop2005': country.pop2005,
                'fips': country.fips,
                'iso2': country.iso2,
                'iso3': country.iso3,
                'un': country.un,
                'region': country.region,
                'subregion': country.subregion,
                'lon': country.lon,
                'lat': country.lat,
            },
        'Date': confirmed.date,
        'Confirmed_total': confirmed.total,
        'Recovered_total': recovered.total,
        'Deaths_total': deaths.total,
        'Bloodtype':
            {
                'Ominus': bloodtype.Ominus,
                'Oplus': bloodtype.Oplus,
                'Aminus': bloodtype.Aminus,
                'Aplus': bloodtype.Aplus,
                'Bminus': bloodtype.Bminus,
                'Bplus': bloodtype.Bplus,
                'ABminus': bloodtype.ABminus,
                'ABplus': bloodtype.ABplus
            },
        'Healthcare':
            {
                'rank': healthcare.rank,
                'score': healthcare.score
            },
        'Smoking':
            {
                'male': smoking.male,
                'female': smoking.female,
                'total': smoking.total
            },
        'GDP':
            {
                'rank': gdp.rank,
                'gdpPerCapita': gdp.gdpPerCapita
            }
    }

    return JsonResponse(all_data)
