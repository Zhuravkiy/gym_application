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
    LocationModelUnrequiredSerializer,
)

from permissions.user_readonly import IsAdminOrReadOnly


class LocationCreateListView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

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


class LocationUpdateRetrieveDeleteView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

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

    @extend_schema(request=LocationModelUnrequiredSerializer)
    def patch(self, request, *args, **kwargs):
        location = get_object_or_404(Location, pk=kwargs.get('pk'))
        serializer = LocationModelUnrequiredSerializer(request.data, partial=True)
        for key, value in serializer.data.items():
            setattr(location, key, value)
        location.save()
        return Response(data=LocationModelSerializer(location).data, status=200)
