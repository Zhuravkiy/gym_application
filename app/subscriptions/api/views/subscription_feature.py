from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from subscriptions.models import (
    SubscriptionFeature,
)
from subscriptions.api.serializers.subscription_feature import (
    SubscriptionFeatureModelSerializer,
    SubscriptionFeatureUnrequiredModelSerializer,
)

from permissions.user_readonly import IsAdminOrReadOnly


class SubscriptionFeatureCreateListView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        """
        Returns list of all Networks
        """
        subscription_plan = SubscriptionFeature.objects.all()
        serializer = SubscriptionFeatureModelSerializer(subscription_plan, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @extend_schema(request=SubscriptionFeatureModelSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new networks
        """
        serializer = SubscriptionFeatureModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription_plan = SubscriptionFeature.objects.create(**serializer.data)

        return Response(data=SubscriptionFeatureModelSerializer(subscription_plan).data, status=HTTP_201_CREATED)


class SubscriptionFeatureUpdateRetrieveDeleteView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        """
        Returns specified network
        """
        subscription_feature = get_object_or_404(SubscriptionFeature, pk=kwargs.get('pk'))
        serializer = SubscriptionFeatureModelSerializer(subscription_feature)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        subscription_feature = get_object_or_404(SubscriptionFeature, pk=kwargs.get('pk'))
        subscription_feature.delete()

        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(request=SubscriptionFeatureUnrequiredModelSerializer)
    def patch(self, request, *args, **kwargs):
        feature = get_object_or_404(SubscriptionFeature, pk=kwargs.get('pk'))
        serializer = SubscriptionFeatureUnrequiredModelSerializer(request.data, partial=True)
        for key, value in serializer.data.items():
            setattr(feature, key, value)
        feature.save()
        return Response(data=SubscriptionFeatureModelSerializer(feature).data, status=200)
