from django.db import models

from Accounts.Models.UserDetails import user_details
from EventRestService.Models.CompanyDetails import Company_Details


class Assign_company(models.Model):
    assign_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Company_Details, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
