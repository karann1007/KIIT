from django.db import models


class Company_Details(models.Model):  # Companies basic information
    comp_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    company_website = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    inception = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name