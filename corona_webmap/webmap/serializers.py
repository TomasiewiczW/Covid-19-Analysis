from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import WorldBorder


class CountrySerializer(GeoFeatureModelSerializer):
    location = GeometrySerializerMethodField()  # allows to compute value during serialization

    def get_location(self, obj):
        return Point(obj.lon, obj.lat)

    class Meta:
        model = WorldBorder
        geo_field = 'location'
        fields = ('name', 'area', 'pop2005')

