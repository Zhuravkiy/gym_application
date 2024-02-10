import pytest

from gyms.models import (
    Network,
)
from gyms.api.serializers.network import (
    NetworkModelSerializer,
)


@pytest.mark.django_db
def test_create_network_ok(api_client, authenticated_admin, network_payload):
    response = api_client.post(
        path='/api/gyms/networks/',
        data=network_payload
    )
    assert response.status_code == 201
    assert Network.objects.get(name=network_payload['name'])


@pytest.mark.django_db
def test_create_network_no_data_error(api_client, authenticated_admin):
    response = api_client.post(
        path='/api/gyms/networks/',
        data={}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_network_ok(api_client, authenticated_admin, created_network):
    response = api_client.get(
        path=f'/api/gyms/networks/{created_network.id}/'
    )
    assert response.status_code == 200
    assert response.json() == NetworkModelSerializer(created_network).data


@pytest.mark.django_db
def test_get_network_wrong_id_error(api_client, authenticated_admin, created_network):
    response = api_client.get(
        path=f'/api/gyms/networks/{created_network.id + 1}/'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_network_ok(api_client, authenticated_admin, created_network):
    test_name = 'test_new_name'
    response = api_client.patch(
        path=f'/api/gyms/networks/{created_network.id}/',
        data={'name': test_name}
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name


@pytest.mark.django_db
def test_update_network_ignore_wrong_data_ok(api_client, authenticated_admin, created_network):
    test_name = 'test_new_name'
    response = api_client.patch(
        path=f'/api/gyms/networks/{created_network.id}/',
        data={
            'wrong_field': test_name,
            'name': test_name
        }
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name


@pytest.mark.django_db
def test_delete_network_ok(api_client, authenticated_admin, created_network):
    response = api_client.delete(
        path=f'/api/gyms/networks/{created_network.id}/'
    )
    assert response.status_code == 204
