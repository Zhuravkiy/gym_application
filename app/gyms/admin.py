from django.contrib import admin
from gyms.models import (
    Network,
    Gym,
    Location,
)

admin.site.register(Network)
admin.site.register(Gym)
admin.site.register(Location)
