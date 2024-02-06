from rest_framework import serializers

from gyms.api.serializers.gym import GymGetSerializer
from subscriptions.api.serializers.subscription_feature import SubscriptionFeatureModelSerializer
from users.models import UserFeature
from users.api.serializers.user import (
    UserModelGetSerializer,
)


class BaseUserSubscriptionFeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFeature
        fields = ('id', 'times_used', 'available')


class UserSubscriptionFeatureGetSerializer(BaseUserSubscriptionFeatureSerializer):
    user = UserModelGetSerializer('user', many=False)
    gym = GymGetSerializer('gym', many=False)
    feature = SubscriptionFeatureModelSerializer('feature', many=False)

    class Meta(BaseUserSubscriptionFeatureSerializer.Meta):
        fields = BaseUserSubscriptionFeatureSerializer.Meta.fields + ('user', 'feature', 'gym', )


class UserSubscriptionFeaturePostSerializer(BaseUserSubscriptionFeatureSerializer):
    user_id = serializers.IntegerField(required=True)
    feature_id = serializers.IntegerField(required=True)
    gym_id = serializers.IntegerField(required=True)

    class Meta(BaseUserSubscriptionFeatureSerializer.Meta):
        fields = BaseUserSubscriptionFeatureSerializer.Meta.fields + ('user_id', 'feature_id', 'gym_id',)

