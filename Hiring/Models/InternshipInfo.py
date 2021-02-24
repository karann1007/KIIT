from django.db import models
from django.db.models import DO_NOTHING

import Hiring
from Accounts.Models.UserDetails import user_details
from EventRestService.Models.CompanyDetails import Company_Details
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream


class internship_info(models.Model):
    internship_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    stream_id = models.ManyToManyField(Stream)
    intern_profile_ctc = models.CharField(max_length=100)
    intern_batch = models.IntegerField()
    intern_offers = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    intern_remark = models.CharField(max_length=100)
    ppo_offered = models.IntegerField()
    ppo_profile_ctc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


