from django.db import models
from django.db.models import DO_NOTHING

import Hiring
from Accounts.Models.UserDetails import user_details
from Scheduler.Models.CompanyDetails import Company_Details
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream


class internship_info(models.Model):
    internship_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    stream_id = models.ManyToManyField(Stream)
    intern_profile_ctc = models.CharField(max_length=100,null=True,blank=True)
    intern_batch = models.IntegerField(null=True,blank=True)
    intern_offers = models.IntegerField(null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    intern_remark = models.CharField(max_length=100,null=True,blank=True)
    ppo_offered = models.IntegerField(null=True,blank=True)
    ppo_profile_ctc = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


