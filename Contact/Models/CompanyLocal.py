from django.db import models

from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.OfficeTypes import Office_Types


class Company_Local(models.Model):  # Companies basic information
    comp_lcl_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(Company_Details,on_delete=models.CASCADE)
    office_id = models.ForeignKey(Office_Types,on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    ho = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,default="India")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

        # return self.company_name