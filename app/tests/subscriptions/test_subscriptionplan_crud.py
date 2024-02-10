import pytest

from subscriptions.models import (
    SubscriptionPlan,
)
from subscriptions.api.serializers.subscription_plan import (
    SubscriptionPlanGetSerializer,
    SubscriptionPlanPostSerializer,
    SubscriptionPlanPatchSerializer,
)


@pytest.mark.django_db
def test_create_plan_ok(api_client, authenticated_admin, plan_payload, created_feature):
    plan_payload['features_id'] = [created_feature.id, ]
    response = api_client.post(
        path='/api/subscriptions/plans/',
        data=plan_payload
    )
    assert response.status_code == 201
    assert SubscriptionPlan.objects.get(
        name=plan_payload['name'],
        price=plan_payload['price']
    )


@pytest.mark.django_db
def test_create_plan_no_data_error(api_client, authenticated_admin):
    response = api_client.post(
        path='/api/subscriptions/plans/',
        data={}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_plan_ok(api_client, authenticated_admin, created_plan):
    response = api_client.get(
        path=f'/api/subscriptions/plans/{created_plan.id}/'
    )
    assert response.status_code == 200
    assert response.json() == SubscriptionPlanGetSerializer(created_plan).data


@pytest.mark.django_db
def test_get_plan_wrong_id_error(api_client, authenticated_admin, created_plan):
    response = api_client.get(
        path=f'/api/subscriptions/plans/{created_plan.id + 1}/'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_plan_ok(api_client, authenticated_admin, created_plan):
    test_name = 'test_new_name'
    test_price = 9.99
    response = api_client.patch(
        path=f'/api/subscriptions/plans/{created_plan.id}/',
        data={'name': test_name, 'price': test_price}
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name
    assert response.json()['price'] == test_price


@pytest.mark.django_db
def test_update_plan_ignore_wrong_data_ok(api_client, authenticated_admin, created_plan):
    test_name = 'test_new_name'
    test_price = 9.99
    response = api_client.patch(
        path=f'/api/subscriptions/plans/{created_plan.id}/',
        data={
            'wrong_field': test_name,
            'name': test_name,
            'price': test_price,
        }
    )
    assert response.status_code == 200
    assert response.json()['name'] == test_name
    assert response.json()['price'] == test_price


@pytest.mark.django_db
def test_delete_plan_ok(api_client, authenticated_admin, created_plan):
    response = api_client.delete(
        path=f'/api/subscriptions/plans/{created_plan.id}/'
    )
    assert response.status_code == 204
