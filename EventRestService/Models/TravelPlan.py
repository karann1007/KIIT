
from django.db import models

from Accounts.Models.UserDetails import user_details


class Travel_Plan(models.Model):

    tr_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    travel_date = models.DateField()
    return_date = models.DateField()
    accompanied_by = models.CharField(max_length=50, null=True, blank=True)
    travel_from = models.CharField(max_length=50)
    travel_to = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50,null=True,blank=True)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

