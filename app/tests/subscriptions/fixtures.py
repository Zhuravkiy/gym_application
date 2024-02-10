import pytest

from subscriptions.models import (
    SubscriptionFeature,
    SubscriptionPlan,
)


@pytest.fixture
def feature_payload():
    payload = {
        'name': 'test_name',
        'amount': 12,
        'infinity': False,
    }
    return payload


@pytest.fixture
def created_feature(api_client, feature_payload):
    feature = SubscriptionFeature(**feature_payload)
    feature.save()
    return feature


@pytest.fixture
def plan_payload():
    payload = {
        'name': 'test_name',
        'price': 4.99
    }
    return payload


@pytest.fixture
def created_plan(api_client, plan_payload, created_feature):
    plan = SubscriptionPlan(**plan_payload)
    plan.save()
    plan.features.add(created_feature)
    return plan
