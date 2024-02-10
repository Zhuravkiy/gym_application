from rest_framework import serializers


class AttendanceSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    feature_id = serializers.IntegerField(required=True)
    gym_id = serializers.IntegerField(required=True)
