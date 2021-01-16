
from django.db import models

from Accounts.Models.UserDetails import user_details


class Internal_Meeting(models.Model): # Internal Meeting activity details

    MEETING = 'ME'
    EMAIL = 'EM'
    PHONE = 'PH'

    MEETING_TYPE_CHOICES = [
        (MEETING, 'Meeting'),
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
    ]

    meet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    meeting_date = models.DateField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    description = models.TextField()
    agenda = models.TextField(null=True,blank=True,default='')
    meeting_type = models.CharField(max_length=2, choices=MEETING_TYPE_CHOICES, default=MEETING)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)