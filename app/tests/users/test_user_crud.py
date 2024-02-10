import pytest

from django.contrib.auth.models import User


from users.api.serializers.user import (
    UserModelGetSerializer
)


@pytest.mark.django_db
def test_create_user_correct_payload_ok(api_client, user_payload):
    # Add password to payload to be able to register
    user_payload['password'] = 'test_password'

    response = api_client.post(
        path='/api/users/',
        data=user_payload
    )
    assert response.status_code == 201
    assert User.objects.get(
        username=user_payload['username'],
        first_name=user_payload['first_name'],
        last_name=user_payload['last_name'],
        email=user_payload['email'],
    )


@pytest.mark.django_db
def test_create_user_wrong_payload_error(api_client, user_payload):
    # user_payload does not contain 'password' field by default
    # endpoint should throw an error because of missing field
    response = api_client.post(
        path='/api/users/',
        data=user_payload
    )
    assert response.status_code == 400
    assert not User.objects.filter(username=user_payload['username'])


@pytest.mark.django_db
def test_get_user_unauthenticated_error(api_client, created_user):
    response = api_client.get(
        path=f'/api/users/{created_user.id}/'
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_user_ok(api_client, authenticated_user):
    response = api_client.get(
        path=f'/api/users/{authenticated_user.id}/'
    )
    assert response.status_code == 200
    assert response.json() == UserModelGetSerializer(authenticated_user).data


@pytest.mark.django_db
def test_update_user_invalid_payload_error(api_client, authenticated_user, user_payload):
    user_payload.pop('username')
    user_payload['email'] = 'test_email@invalid@structure'
    response = api_client.patch(
        path=f'/api/users/{authenticated_user.id}/',
        data=user_payload
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_update_user_ok(api_client, authenticated_user, user_payload):
    user_payload.pop('username')
    response = api_client.patch(
        path=f'/api/users/{authenticated_user.id}/',
        data=user_payload
    )
    assert response.status_code == 200
    assert response.json() == UserModelGetSerializer(authenticated_user).data


@pytest.mark.django_db
def test_delete_user_ok(api_client, authenticated_user):
    response = api_client.delete(
        path=f'/api/users/{authenticated_user.id}/'
    )
    assert response.status_code == 204
