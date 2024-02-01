from rest_framework import serializers

from gyms.models import (
    Location,
)


class LocationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
