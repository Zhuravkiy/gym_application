from django.db import models

from subscriptions.models import (
    SubscriptionPlan,
    SubscriptionFeature,
)


class Network(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, default="Базовая сеть спортзалов")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Gym(models.Model):
    network = models.ForeignKey('Network', null=True, on_delete=models.SET_NULL)
    coordinates = models.OneToOneField('Location', null=True, on_delete=models.SET_NULL)
    name = models.CharField(null=False, blank=False, max_length=255, default="Базовый план")
    description = models.TextField(null=True, default=None)
    plans = models.ManyToManyField(SubscriptionPlan)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Location(models.Model):
    country = models.CharField(null=False, blank=False, max_length=255, default="Беларусь")
    city = models.CharField(null=False, blank=False, max_length=255, default="Минск")
    street = models.CharField(null=False, blank=False, max_length=255)
    building = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.country}: {self.city}, {self.street}, {self.building}"
