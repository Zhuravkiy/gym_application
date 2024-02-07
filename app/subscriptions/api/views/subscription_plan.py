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
    SubscriptionPlan,
    SubscriptionFeature,
)
from subscriptions.api.serializers.subscription_plan import (
    SubscriptionPlanGetSerializer,
    SubscriptionPlanPostSerializer,
)
from subscriptions.models import (
    SubscriptionFeature,
)

from permissions.user_readonly import IsAdminOrReadOnly


class SubscriptionPlanCreateListView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        """
        Returns list of all SubscriptionPlans
        """
        subscription_plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanGetSerializer(subscription_plans, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @extend_schema(request=SubscriptionPlanPostSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new subscription plans
        """
        serializer = SubscriptionPlanPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription_plan = SubscriptionPlan.objects.create(
            name=serializer.data['name'],
            price=serializer.data['price'],
        )
        subscription_plan.features.set(SubscriptionFeature.objects.filter(id__in=serializer.data['features_id']))

        return Response(data=SubscriptionPlanGetSerializer(subscription_plan).data, status=HTTP_201_CREATED)


class SubscriptionPlanRetrieveDeleteView(views.APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        """
        Returns specified network
        """
        subscription_plan = get_object_or_404(SubscriptionPlan, pk=kwargs.get('pk'))
        serializer = SubscriptionPlanGetSerializer(subscription_plan)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        subscription_plan = get_object_or_404(SubscriptionPlan, pk=kwargs.get('pk'))
        subscription_plan.delete()

        return Response(status=HTTP_204_NO_CONTENT)
