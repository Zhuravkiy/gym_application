import pytest


@pytest.mark.django_db
def test_create_gym_ok(
        api_client,
        authenticated_admin,
        gym_payload,
        network_payload,
        location_payload,
        created_location,
        created_network
):
    gym_payload['location_id'] = created_location.id
    gym_payload['network_id'] = created_network.id
    gym_payload['plans_id'] = [0, ]
    response = api_client.post(
        path='/api/gyms/',
        data=gym_payload
    )
    assert response.status_code == 201
    assert response.json()['name'] == gym_payload['name']
    assert response.json()['description'] == gym_payload['description']
    assert response.json()['network']['id'] == gym_payload['network_id']
    assert response.json()['location']['id'] == gym_payload['location_id']
    assert response.json()['plans'] == []


@pytest.mark.django_db
def test_create_gym_no_data_error(api_client, authenticated_admin):
    response = api_client.post(
        path='/api/gyms/',
        data={}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_gym_ok(api_client, authenticated_admin, created_gym):
    response = api_client.get(
        path=f'/api/gyms/{created_gym.id}/'
    )
    assert response.status_code == 200
    assert response.json()['name'] == created_gym.name
    assert response.json()['description'] == created_gym.description
    assert response.json()['network']['id'] == created_gym.network.id
    assert response.json()['location']['id'] == created_gym.location.id
    assert response.json()['plans'] == []


@pytest.mark.django_db
def test_get_all_gyms_ok(api_client, authenticated_admin, created_gym):
    response = api_client.get(
        path=f'/api/gyms/'
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == created_gym.name



@pytest.mark.django_db
def test_get_gym_wrong_id_error(api_client, authenticated_admin, created_gym):
    response = api_client.get(
        path=f'/api/gyms/{created_gym.id + 1}/'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_gym_ok(api_client, authenticated_admin, created_gym):
    test_name = 'test_new_name'
    response = api_client.patch(
        path=f'/api/gyms/{created_gym.id}/',
        data={'name': test_name}
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name


@pytest.mark.django_db
def test_update_gym_ignore_wrong_data_ok(api_client, authenticated_admin, created_gym):
    test_name = 'test_new_name'
    response = api_client.patch(
        path=f'/api/gyms/{created_gym.id}/',
        data={
            'wrong_field': test_name,
            'name': test_name
        }
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name


@pytest.mark.django_db
def test_delete_gym_ok(api_client, authenticated_admin, created_gym):
    response = api_client.delete(
        path=f'/api/gyms/{created_gym.id}/'
    )
    assert response.status_code == 204
