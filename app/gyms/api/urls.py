from rest_framework.urls import path

from gyms.api.views.network import (
    NetworkCreateListView,
    NetworkRetrieveDeleteView,
)
from gyms.api.views.location import (
    LocationCreateListView,
    LocationRetrieveDeleteView,
)
from gyms.api.views.gym import (
    GymCreateListView,
    GymRetrieveDeleteView,
)


urlpatterns = [
    # Gyms
    path('', GymCreateListView.as_view()),
    path('<int:pk>/', GymRetrieveDeleteView.as_view()),

    # Networks
    path('networks/', NetworkCreateListView.as_view()),
    path('networks/<int:pk>/', NetworkRetrieveDeleteView.as_view()),

    # Locations
    path('locations/', LocationCreateListView.as_view()),
    path('locations/<int:pk>/', LocationRetrieveDeleteView.as_view()),
]
