from django.contrib.auth.models import User
from rest_framework import serializers


class UserModelGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'last_login', 'username', 'first_name', 'last_name',
            'email', 'is_staff', 'is_active', 'date_joined'
        )


class UserModelPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserModelPatchSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserModelPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', )
