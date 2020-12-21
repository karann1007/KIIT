from Accounts.Models.UserDetails import user_details
from django.db import models

from EventRestService.Models.CompanyDetails import Company_Details
from EventRestService.Models.ContactAlumini import Contact_alumini


class External_Meetings(models.Model):  # Client meeting activity details

    MEETING = 'ME'
    EMAIL = 'EM'
    PHONE = 'PH'

    MEETING_TYPE_CHOICES = [
        (MEETING, 'Meeting'),
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
    ]

    meet_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contact_alumini, on_delete=models.CASCADE)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None)
    agenda = models.CharField(max_length=150,null=True,blank=True,default=None)
    meeting_date = models.DateField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    location = models.CharField(max_length=100)
    assigned_to = models.TextField(null=True , blank= True)
    reference = models.CharField(max_length=100,blank=True,null=True,default="")
    meeting_type = models.CharField(max_length=2, choices=MEETING_TYPE_CHOICES, default=MEETING)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)