from rest_framework import serializers

from gyms.models import (
    Network,
)


class NetworkModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Network
        fields = ['id', 'name']


class NetworkModelUnrequiredSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Network
        fields = ['id', 'name']
