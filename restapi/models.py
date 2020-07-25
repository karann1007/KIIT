from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    time = models.BigIntegerField(null=False, blank=False)
    date = models.DateField(unique=True, null=False)
    location = models.CharField(max_length=256)
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)
