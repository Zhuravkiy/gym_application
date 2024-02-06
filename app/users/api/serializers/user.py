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


class UserModelPasswordSerialzier(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', )
