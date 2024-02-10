import pytest

from gyms.models import (
    Gym,
    Network,
    Location,
)


@pytest.fixture
def network_payload():
    payload = {
        'name': 'test_name',
    }
    return payload


@pytest.fixture
def created_network(api_client, network_payload):
    network = Network(**network_payload)
    network.save()
    return network


@pytest.fixture
def location_payload():
    payload = {
        'country': 'test_country',
        'city': 'test_city',
        'street': 'test_street',
        'building': '1A',
    }
    return payload


@pytest.fixture
def created_location(api_client, location_payload):
    location = Location(**location_payload)
    location.save()
    return location


@pytest.fixture
def gym_payload():
    payload = {
        'name': 'test_name',
        'description': 'test_description'
    }
    return payload


@pytest.fixture
def created_gym(api_client, gym_payload, created_location, created_network):
    gym = Gym(**gym_payload, network_id=created_network.id, location_id=created_location.id)
    gym.save()
    return gym
