from django.db import models


class SubscriptionFeature(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    amount = models.IntegerField(null=True, blank=True, default=8)
    infinity = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class SubscriptionPlan(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    price = models.FloatField(null=False, default=9.99)
    features = models.ManyToManyField('SubscriptionFeature')

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"