from rest_framework.urls import path

from users.api.views.user import (
    UserCreateView,
    UserUpdateRetrieveDeleteView,
    UserChangePasswordView,
)
from users.api.views.user_feature import (
    UserSubscriptionFeatureListView,
    UserSubscriptionFeatureRetrieveDeleteView,
)


urlpatterns = [
    # Users
    path('', UserCreateView.as_view()),
    path('<int:pk>/', UserUpdateRetrieveDeleteView.as_view()),
    path('<int:pk>/password/', UserChangePasswordView.as_view()),

    # UserFeatures
    path('accessability/', UserSubscriptionFeatureListView.as_view()),
    path('<int:pk>/accessability/', UserSubscriptionFeatureRetrieveDeleteView.as_view()),
]
