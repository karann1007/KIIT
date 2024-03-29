from django.db import models

from Accounts.Models.UserDetails import user_details
from Scheduler.Models.CompanyDetails import Company_Details
from Hiring.Models.PlacementStatus import Placement_Status
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream


class placement_info(models.Model):
    placement_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    stream_id = models.ManyToManyField(Stream)
    placement_status_id = models.IntegerField(null=True,blank=True)
    profile_ctc = models.CharField(max_length=100,null=True,blank=True)
    batch = models.IntegerField(null=True,blank=True)
    offers = models.IntegerField(null=True,blank=True)
    visit_month = models.CharField(max_length=100,null=True,blank=True)
    remark = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



