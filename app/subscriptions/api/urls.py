from rest_framework.urls import path

from subscriptions.api.views.subscription_feature import (
    SubscriptionFeatureCreateListView,
    SubscriptionFeatureRetrieveDeleteView,
)
from subscriptions.api.views.subscription_plan import (
    SubscriptionPlanCreateListView,
    SubscriptionPlanRetrieveDeleteView,
)
from subscriptions.api.views.attendance import AttendanceCallback


urlpatterns = [
    # Subscription Features
    path('features/', SubscriptionFeatureCreateListView.as_view()),
    path('features/<int:pk>/', SubscriptionFeatureRetrieveDeleteView.as_view()),

    # Subscription Plans
    path('plans/', SubscriptionPlanCreateListView.as_view()),
    path('plans/<int:pk>/', SubscriptionPlanRetrieveDeleteView.as_view()),

    # Attendance Tracking
    path('callback/attend/', AttendanceCallback.as_view())
]
