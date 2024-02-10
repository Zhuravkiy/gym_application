import pytest

from gyms.models import (
    Location,
)
from gyms.api.serializers.location import (
    LocationModelSerializer,
)


@pytest.mark.django_db
def test_create_location_ok(api_client, authenticated_admin, location_payload):
    response = api_client.post(
        path='/api/gyms/locations/',
        data=location_payload
    )
    assert response.status_code == 201
    assert Location.objects.get(
        country=location_payload['country'],
        city=location_payload['city'],
        street=location_payload['street'],
        building=location_payload['building']
    )


@pytest.mark.django_db
def test_create_location_no_data_error(api_client, authenticated_admin):
    response = api_client.post(
        path='/api/gyms/locations/',
        data={}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_location_ok(api_client, authenticated_admin, created_location):
    response = api_client.get(
        path=f'/api/gyms/locations/{created_location.id}/'
    )
    assert response.status_code == 200
    assert response.json() == LocationModelSerializer(created_location).data


@pytest.mark.django_db
def test_get_location_wrong_id_error(api_client, authenticated_admin, created_location):
    response = api_client.get(
        path=f'/api/gyms/locations/{created_location.id + 1}/'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_location_ok(api_client, authenticated_admin, created_location):
    test_country = 'test_new_country'
    response = api_client.patch(
        path=f'/api/gyms/locations/{created_location.id}/',
        data={'country': test_country}
    )
    assert response.status_code == 200
    assert response.json()['country'] == test_country


@pytest.mark.django_db
def test_update_location_ignore_wrong_data_ok(api_client, authenticated_admin, created_location):
    test_country = 'test_new_country'
    response = api_client.patch(
        path=f'/api/gyms/locations/{created_location.id}/',
        data={
            'wrong_field': test_country,
            'country': test_country
        }
    )
    assert response.status_code == 200
    assert response.json()['country'] == test_country


@pytest.mark.django_db
def test_delete_network_ok(api_client, authenticated_admin, created_location):
    response = api_client.delete(
        path=f'/api/gyms/locations/{created_location.id}/'
    )
    assert response.status_code == 204
