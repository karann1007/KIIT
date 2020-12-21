from django.contrib.auth.models import User, UserManager
from django.db import models

class user_details(User):
    mobile = models.IntegerField(null=True)
    address = models.TextField(null=True)
    usertype = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, default="")
    zone = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()