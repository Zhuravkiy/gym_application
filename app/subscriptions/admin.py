from django.contrib import admin
from subscriptions.models import (
    SubscriptionPlan,
    SubscriptionFeature,
)

admin.site.register(SubscriptionPlan)
admin.site.register(SubscriptionFeature)
