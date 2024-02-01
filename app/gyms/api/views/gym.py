from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from gyms.models import (
    Network,
    Location,
    Gym,
)
from gyms.api.serializers.gym import (
    GymGetSerializer,
    GymPostSerializer,
)
from subscriptions.models import (
    SubscriptionPlan,
)


class GymCreateListView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns list of all Networks
        """
        gyms = Gym.objects.all()
        serializer = GymGetSerializer(gyms, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=GymPostSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new networks
        """
        serializer = GymPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gym = Gym.objects.create(
            network=get_object_or_404(Network, id=serializer.data['network_id']),
            location=get_object_or_404(Location, id=serializer.data['location_id']),
            name=serializer.data['name'],
            description=serializer.data['description'],
        )
        gym.plans.set(SubscriptionPlan.objects.filter(id__in=serializer.data['plans_id']))

        return Response(data=GymGetSerializer(gym).data, status=HTTP_201_CREATED)


class GymRetrieveDeleteView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns specified network
        """
        gym = get_object_or_404(Gym, pk=kwargs.get('pk'))
        serializer = GymGetSerializer(gym)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        gym = get_object_or_404(Gym, pk=kwargs.get('pk'))
        gym.delete()

        return Response(status=HTTP_204_NO_CONTENT)
