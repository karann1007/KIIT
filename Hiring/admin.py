from django.contrib import admin

# Register your models here.
from Hiring.Models.AssignCompany import Assign_company
from Hiring.Models.InternshipInfo import internship_info
from Hiring.Models.PlacementInfo import placement_info
from Hiring.Models.PlacementStatus import Placement_Status
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream

admin.site.register(Assign_company)
admin.site.register(internship_info)
admin.site.register(placement_info)
admin.site.register(Placement_Status)
admin.site.register(School)
admin.site.register(Stream)

