from django.db import models


class Address(models.Model):
    description = models.CharField(max_length=1024, )
    ville = models.CharField(max_length=1024, null=True)
    latitude = models.FloatField(max_length=120, null=True)
    longitude = models.FloatField(max_length=120, null=True)
