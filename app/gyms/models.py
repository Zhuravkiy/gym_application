from django.db import models

from subscriptions.models import (
    SubscriptionPlan,
    SubscriptionFeature,
)


class Network(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, default="Gym Network")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Gym(models.Model):
    network = models.ForeignKey('Network', null=True, on_delete=models.SET_NULL)
    coordinates = models.OneToOneField('Coordinates', null=True, on_delete=models.SET_NULL)
    name = models.CharField(null=False, blank=False, max_length=255, default="Basic Place")
    description = models.TextField(null=True, default=None)
    plans = models.ManyToManyField(SubscriptionPlan)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Coordinates(models.Model):
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.longitude} {self.latitude}"
