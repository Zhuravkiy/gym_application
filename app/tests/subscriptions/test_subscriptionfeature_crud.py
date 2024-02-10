import pytest

from subscriptions.models import (
    SubscriptionFeature,
)
from subscriptions.api.serializers.subscription_feature import (
    SubscriptionFeatureModelSerializer,
)


@pytest.mark.django_db
def test_create_feature_ok(api_client, authenticated_admin, feature_payload):
    response = api_client.post(
        path='/api/subscriptions/features/',
        data=feature_payload
    )
    assert response.status_code == 201
    assert SubscriptionFeature.objects.get(
        name=feature_payload['name'],
        amount=feature_payload['amount'],
    )


@pytest.mark.django_db
def test_create_feature_no_data_error(api_client, authenticated_admin):
    response = api_client.post(
        path='/api/subscriptions/features/',
        data={}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_feature_ok(api_client, authenticated_admin, created_feature):
    response = api_client.get(
        path=f'/api/subscriptions/features/{created_feature.id}/'
    )
    assert response.status_code == 200
    assert response.json() == SubscriptionFeatureModelSerializer(created_feature).data


@pytest.mark.django_db
def test_get_feature_wrong_id_error(api_client, authenticated_admin, created_feature):
    response = api_client.get(
        path=f'/api/subscriptions/features/{created_feature.id + 1}/'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_feature_ok(api_client, authenticated_admin, created_feature):
    test_name = 'test_new_name'
    test_amount = 12
    response = api_client.patch(
        path=f'/api/subscriptions/features/{created_feature.id}/',
        data={'name': test_name, 'amount': test_amount}
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name
    assert response.json()['amount'] == test_amount


@pytest.mark.django_db
def test_update_feature_ignore_wrong_data_ok(api_client, authenticated_admin, created_feature):
    test_name = 'test_new_name'
    test_amount = 12
    response = api_client.patch(
        path=f'/api/subscriptions/features/{created_feature.id}/',
        data={
            'wrong_field': test_name,
            'name': test_name,
            'amount': test_amount,
        }
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name
    assert response.json()['amount'] == test_amount

@pytest.mark.django_db
def test_delete_feature_ok(api_client, authenticated_admin, created_feature):
    response = api_client.delete(
        path=f'/api/subscriptions/features/{created_feature.id}/'
    )
    assert response.status_code == 204
