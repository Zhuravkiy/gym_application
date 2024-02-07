import datetime

from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
)

from gyms.models import Gym
from subscriptions.models import SubscriptionFeature
from users.api.serializers.user_feature import (
    UserSubscriptionFeatureGetSerializer,
    UserSubscriptionFeaturePostSerializer,
)
from users.models import UserFeature


class UserSubscriptionFeatureListView(views.APIView):
    permission_classes = (IsAdminUser, )

    def get(self, request, *args, **kwargs):
        """
        Returns list of all UserFeature
        """
        user_features = UserFeature.objects.all()
        serializer = UserSubscriptionFeatureGetSerializer(user_features, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @extend_schema(request=UserSubscriptionFeaturePostSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new UserFeature
        """
        serializer = UserSubscriptionFeaturePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_feature = UserFeature(
            times_used=serializer.data['times_used'],
            available=serializer.data['available'],
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now() + datetime.timedelta(days=30)
        )
        user_feature.feature = get_object_or_404(SubscriptionFeature, id=serializer.data['feature_id'])
        user_feature.user = get_object_or_404(User, id=serializer.data['user_id'])
        user_feature.gym = get_object_or_404(Gym, id=serializer.data['gym_id'])
        user_feature.save()

        return Response(data=UserSubscriptionFeatureGetSerializer(user_feature).data, status=HTTP_201_CREATED)


class UserSubscriptionFeatureRetrieveDeleteView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        """
        Returns specified UserFeature
        """
        user_feature = get_object_or_404(UserFeature, user_id=kwargs.get('pk'))
        serializer = UserSubscriptionFeatureGetSerializer(user_feature)

        return Response(data=serializer.data, status=HTTP_200_OK)
