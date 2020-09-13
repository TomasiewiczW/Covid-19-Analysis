from rest_framework import serializers
from django.db.models import Max
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import Confirmed, WorldBorder


class CovidConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmed
        fields = ('total', )


class CountrySerializer(GeoFeatureModelSerializer):
    current_total = serializers.SerializerMethodField("get_current_total")
    location = GeometrySerializerMethodField()  # allows to compute value during serialization

    def get_current_total(self, country):  # SerializerMethodField automatically infers callback from variable name
        try:
            items = Confirmed.objects.filter(country=country.pk).latest('date')
        except Confirmed.DoesNotExist:
            items = Confirmed(country=country, date=None, total=None)
        serializer = CovidConfirmedSerializer(instance=items)
        return serializer.data

    def get_location(self, obj):
        return Point(obj.lon, obj.lat)

    class Meta:
        model = WorldBorder
        geo_field = 'location'
        fields = ('name', 'pop2005', 'current_total', )


class SelectedGeometrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = 'mpoly'
        fields = ('name',)
