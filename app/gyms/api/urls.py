from rest_framework.urls import path

from gyms.api.views.network import (
    NetworkCreateListView,
    NetworkUpdateRetrieveDeleteView,
)
from gyms.api.views.location import (
    LocationCreateListView,
    LocationUpdateRetrieveDeleteView,
)
from gyms.api.views.gym import (
    GymCreateListView,
    GymUpdateRetrieveDeleteView,
)


urlpatterns = [
    # Gyms
    path('', GymCreateListView.as_view()),
    path('<int:pk>/', GymUpdateRetrieveDeleteView.as_view()),

    # Networks
    path('networks/', NetworkCreateListView.as_view()),
    path('networks/<int:pk>/', NetworkUpdateRetrieveDeleteView.as_view()),

    # Locations
    path('locations/', LocationCreateListView.as_view()),
    path('locations/<int:pk>/', LocationUpdateRetrieveDeleteView.as_view()),
]
