import pytz

from datetime import datetime

from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from subscriptions.api.serializers.attendance import AttendanceSerializer
from users.models import UserFeature


class AttendanceCallback(APIView):

    @extend_schema(request=AttendanceSerializer)
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_feature = get_object_or_404(
            UserFeature,
            user_id=serializer.data['user_id'],
            gym_id=serializer.data['gym_id'],
            feature_id=serializer.data['feature_id'],
        )

        if user_feature.available is False:
            return Response({"approved": False}, status=HTTP_200_OK)
        if user_feature.end_date < pytz.UTC.localize(datetime.now()) or (
            user_feature.times_used >= (user_feature.feature.amount or 0) and user_feature.feature.infinity is False
        ):
            user_feature.available = False
            return Response({"approved": False}, status=HTTP_200_OK)

        user_feature.times_used += 1
        user_feature.save()

        return Response({"approved": True}, status=HTTP_200_OK)
