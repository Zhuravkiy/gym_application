from rest_framework import serializers

from subscriptions.models import (
    SubscriptionPlan,
)
from subscriptions.api.serializers.subscription_feature import (
    SubscriptionFeatureModelSerializer,
)


class BaseSubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = ('id', 'name', 'price')


class SubscriptionPlanGetSerializer(BaseSubscriptionPlanSerializer):
    features = SubscriptionFeatureModelSerializer('plans', many=True)

    class Meta(BaseSubscriptionPlanSerializer.Meta):
        fields = BaseSubscriptionPlanSerializer.Meta.fields + ('features', )


class SubscriptionPlanPostSerializer(BaseSubscriptionPlanSerializer):
    features_id = serializers.ListField(child=serializers.IntegerField())

    class Meta(BaseSubscriptionPlanSerializer.Meta):
        fields = BaseSubscriptionPlanSerializer.Meta.fields + ('features_id', )

