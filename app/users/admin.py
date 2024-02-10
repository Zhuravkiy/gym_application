from django.contrib import admin
from django.contrib.auth.models import (
    Group,
)

from users.models import UserFeature

admin.site.unregister(Group)
admin.site.register(UserFeature)
