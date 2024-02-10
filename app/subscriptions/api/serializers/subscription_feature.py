from rest_framework import serializers

from subscriptions.models import (
    SubscriptionFeature,
)


class SubscriptionFeatureModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionFeature
        fields = '__all__'


class SubscriptionFeatureUnrequiredModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=False)
    infinity = serializers.BooleanField(required=False)

    class Meta:
        model = SubscriptionFeature
        fields = '__all__'
