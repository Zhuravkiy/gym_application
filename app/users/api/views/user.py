from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from users.api.serializers.user import (
    UserModelGetSerializer,
    UserModelPostSerializer,
    UserModelPasswordSerialzier,
)
from permissions.anon_postonly import IsAuthenticatedOrPostOnly


class UserCreateView(views.APIView):
    permission_classes = (IsAuthenticatedOrPostOnly, )

    @extend_schema(request=UserModelPostSerializer)
    def post(self, request, *args, **kwargs):
        """
        Give ability to create new User
        """
        serializer = UserModelPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            first_name=serializer.data['first_name'],
            last_name=serializer.data['last_name'],
            email=serializer.data['email'],
            username=serializer.data['username'],
            password=serializer.data['password']
        )

        return Response(data=UserModelGetSerializer(user).data, status=HTTP_201_CREATED)


class UserRetrieveDeleteView(views.APIView):
    permission_classes = (IsAuthenticatedOrPostOnly, )

    def get(self, request, *args, **kwargs):
        """
        Returns specified User
        """
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        serializer = UserModelGetSerializer(user)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete specified network
        """
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        user.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class UserChangePasswordView(views.APIView):
    permission_classes = (IsAdminUser, )

    @extend_schema(request=UserModelPasswordSerialzier)
    def post(self, request, *args, **kwargs):
        serializer = UserModelPasswordSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        user.set_password(serializer.data['password'])
        user.save()

        return Response(status=HTTP_204_NO_CONTENT)
