from django.db import models
from Accounts.Models.UserDetails import user_details
from EventRestService.Models.CompanyDetails import Company_Details
from EventRestService.Models.OfficeTypes import Office_Types


class Contact_alumini(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)  #int
    contact_name = models.CharField(max_length=50)
    referred_by = models.CharField(max_length=50)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    direct_number = models.CharField(max_length=50)
    notes = models.TextField()
    institution = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    total_experience = models.DurationField()
    yop = models.IntegerField()
    degree = models.CharField(max_length=50)
    current_experience = models.DurationField()
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    office_id = models.ForeignKey(Office_Types, on_delete=models.CASCADE)
    address = models.TextField()
    board_line_no = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pin = models.IntegerField()
    recruitment = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name