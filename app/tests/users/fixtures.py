import random
import pytest
from django.contrib.auth.models import User
from users.models import UserFeature


@pytest.fixture
def user_payload():
    payload = {
        'username': f'user_{random.randrange(1,1000000)}',
        'first_name': 'test_first_name',
        'last_name': 'test_last_name',
        'email': 'test@example.com'
    }
    return payload


@pytest.fixture
def created_user(user_payload):
    user = User(**user_payload)
    user.set_password('test_password')
    user.save()
    return user


@pytest.fixture
def authenticated_user(api_client, created_user):
    api_client.force_authenticate(created_user)
    return created_user


@pytest.fixture
def authenticated_admin(api_client, created_user):
    created_user.is_staff = True
    created_user.is_superuser = True
    api_client.force_authenticate(created_user)
    return created_user
