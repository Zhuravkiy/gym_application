from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from gyms.models import Gym
from subscriptions.models import SubscriptionFeature


class UserFeature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usersubscriptions')
    feature = models.ForeignKey(SubscriptionFeature, on_delete=models.CASCADE, related_name='userfeatures')
    gym = models.ForeignKey(Gym, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(null=False, editable=False, default=timezone.now)
    end_date = models.DateTimeField(null=False, editable=False, default=timezone.now)
    times_used = models.IntegerField(null=False, default=0)
    available = models.BooleanField(null=False, default=True)
