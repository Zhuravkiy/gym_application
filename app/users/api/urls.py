from rest_framework.urls import path

from users.api.views.user import (
    UserCreateView,
    UserRetrieveDeleteView,
    UserChangePasswordView,
)
from users.api.views.user_feature import (
    UserSubscriptionFeatureListView,
    UserSubscriptionFeatureRetrieveDeleteView,
)


urlpatterns = [
    # Users
    path('', UserCreateView.as_view()),
    path('<int:pk>/', UserRetrieveDeleteView.as_view()),
    path('<int:pk>/password/', UserChangePasswordView.as_view()),

    # UserFeatures
    path('subscription_features/', UserSubscriptionFeatureListView.as_view()),
    path('<int:pk>/subscription_features/', UserSubscriptionFeatureRetrieveDeleteView.as_view()),
]
