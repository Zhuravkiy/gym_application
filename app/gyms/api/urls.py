from rest_framework.urls import path

from gyms.api.views.network import (
    NetworkCreateListView,
    NetworkRetrieveDeleteView,
)


urlpatterns = [
    # Networks
    path('networks/', NetworkCreateListView.as_view()),
    path('networks/<int:pk>/', NetworkRetrieveDeleteView.as_view()),

    # Gyms
    # TODO
]
