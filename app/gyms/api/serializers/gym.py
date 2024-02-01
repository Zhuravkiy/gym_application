from rest_framework import serializers

from gyms.models import (
    Gym,
)
from gyms.api.serializers.location import (
    LocationModelSerializer,
)
from gyms.api.serializers.network import (
    NetworkModelSerializer,
)
from subscriptions.api.serializers.subscription_plan import (
    SubscriptionPlanGetSerializer,
)


class BaseGymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = ('id', 'name', 'description', )


class GymGetSerializer(BaseGymSerializer):
    network = NetworkModelSerializer('network')
    location = LocationModelSerializer('location')
    plans = SubscriptionPlanGetSerializer('plans', many=True)

    class Meta(BaseGymSerializer.Meta):
        fields = BaseGymSerializer.Meta.fields + ('network', 'location', 'plans', )


class GymPostSerializer(BaseGymSerializer):
    network_id = serializers.IntegerField()
    location_id = serializers.IntegerField()
    plans_id = serializers.ListField(child=serializers.IntegerField())

    class Meta(BaseGymSerializer.Meta):
        fields = BaseGymSerializer.Meta.fields + ('network_id', 'location_id', 'plans_id', )
