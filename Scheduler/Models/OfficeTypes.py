from django.db import models


class Office_Types(models.Model):  # Basic information about office types
    office_id = models.AutoField(primary_key=True)
    office_types = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)