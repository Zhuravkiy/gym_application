from rest_framework import serializers

from gyms.models import (
    Location,
)


class LocationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class LocationModelUnrequiredSerializer(serializers.ModelSerializer):
    country = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    street = serializers.CharField(required=False)
    building = serializers.CharField(required=False)

    class Meta:
        model = Location
        fields = ('country', 'city', 'street', 'building')
