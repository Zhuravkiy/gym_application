from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from gyms.models import (
    Location,
)
from gyms.api.serializers.location import (
    LocationModelSerializer,
)


class LocationCreateListView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns list of all Networks
        """
        networks = Location.objects.all()
        serializer = LocationModelSerializer(networks, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @extend_schema(request=LocationModelSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new networks
        """
        serializer = LocationModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location = Location.objects.create(**serializer.data)

        return Response(data=LocationModelSerializer(location).data, status=HTTP_201_CREATED)


class LocationRetrieveDeleteView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns specified network
        """
        network = get_object_or_404(Location, pk=kwargs.get('pk'))
        serializer = LocationModelSerializer(network)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        network = get_object_or_404(Location, pk=kwargs.get('pk'))
        network.delete()

        return Response(status=HTTP_204_NO_CONTENT)
