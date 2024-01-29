from django.contrib import admin
from gyms.models import (
    Network,
    Gym,
    Coordinates,
)

admin.site.register(Network)
admin.site.register(Gym)
admin.site.register(Coordinates)
