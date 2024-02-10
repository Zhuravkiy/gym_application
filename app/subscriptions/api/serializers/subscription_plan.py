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
    features = SubscriptionFeatureModelSerializer('features', many=True)

    class Meta(BaseSubscriptionPlanSerializer.Meta):
        fields = BaseSubscriptionPlanSerializer.Meta.fields + ('features', )


class SubscriptionPlanPostSerializer(BaseSubscriptionPlanSerializer):
    features_id = serializers.ListField(child=serializers.IntegerField())

    class Meta(BaseSubscriptionPlanSerializer.Meta):
        fields = BaseSubscriptionPlanSerializer.Meta.fields + ('features_id', )


class SubscriptionPlanPatchSerializer(BaseSubscriptionPlanSerializer):
    name = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    features_id = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta(BaseSubscriptionPlanSerializer.Meta):
        fields = BaseSubscriptionPlanSerializer.Meta.fields + ('features_id', )

