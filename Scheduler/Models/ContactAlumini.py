from django.db import models
from Accounts.Models.UserDetails import user_details
from Contact.Models.CompanyLocal import Company_Local
from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.OfficeTypes import Office_Types


class Contact_alumini(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    # office_id = models.ForeignKey(Office_Types, blank=True, null=True)
    comp_lcl_id = models.ForeignKey(Company_Local,on_delete=models.CASCADE,blank=True,null=True)
    contact_name = models.CharField(max_length=50)
    referred_by = models.CharField(max_length=50)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=100,null=True,blank=True)
    direct_number = models.CharField(max_length=50)
    notes = models.TextField()
    institution = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    total_experience = models.DurationField(blank=True,null=True)
    year = models.IntegerField()
    month = models.IntegerField()
    yop = models.IntegerField()
    degree = models.CharField(max_length=50)
    current_experience = models.DurationField(blank=True,null=True)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    recruitment = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name