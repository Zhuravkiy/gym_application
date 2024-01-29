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
)
from gyms.api.serializers.network import (
    NetworkModelSerializer,
)


class NetworkCreateListView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns list of all Networks
        """
        networks = Network.objects.all()
        serializer = NetworkModelSerializer(networks, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=NetworkModelSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new networks
        """
        serializer = NetworkModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Network.objects.create(**serializer.data)

        return Response(data=serializer.data, status=HTTP_201_CREATED)


class NetworkRetrieveDeleteView(views.APIView):

    def get(self, request, *args, **kwargs):
        """
        Returns specified network
        """
        network = get_object_or_404(Network, pk=kwargs.get('pk'))
        serializer = NetworkModelSerializer(network)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        network = get_object_or_404(Network, pk=kwargs.get('pk'))
        network.delete()

        return Response(status=HTTP_204_NO_CONTENT)
