from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from webmap import models

from .serializers import CountrySerializer, SelectedGeometrySerializer
from webmap import models

from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    template_name = "webmap/map.html"

    
@api_view(['GET'])
def dataLoad(request,pk):


    #main class
    try:
        country = models.WorldBorder.objects.get(name=pk)
    except models.WorldBorder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    #supplemental data
    gdp = models.GDP.objects.get(country_id=country.name)
    smoking = models.Smoking.objects.get(country_id=country.name)
    healthcare = models.Healthcare.objects.get(country_id=country.name)
    bloodtype = models.Bloodtype.objects.get(country_id=country.name)

    #covid data
    confirmed = models.Confirmed.objects.filter(country_id=country.name).latest('date')
    recovered = models.Recovered.objects.filter(country_id=country.name).latest('date')
    deaths = models.Deaths.objects.filter(country_id=country.name).latest('date')


    all_data = {
        'Country':
            {
                'name': country.name,
                'area': country.area,
                'pop2005':country.pop2005,
                'fips': country.fips,
                'iso2': country.iso2,
                'iso3': country.iso3,
                'un': country.un,
                'region': country.region,
                'subregion': country.subregion,
                'lon':country.lon,
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
