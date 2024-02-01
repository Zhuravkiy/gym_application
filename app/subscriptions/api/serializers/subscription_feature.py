from rest_framework import serializers

from subscriptions.models import (
    SubscriptionFeature,
)


class SubscriptionFeatureModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionFeature
        fields = '__all__'
