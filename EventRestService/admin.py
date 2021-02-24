from django.contrib import admin

# Register your models here.
from Hiring.Models.AssignCompany import Assign_company
from EventRestService.Models.CompanyDetails import Company_Details
from EventRestService.Models.ContactAlumini import Contact_alumini
from EventRestService.Models.ExternalMeetings import External_Meetings
from EventRestService.Models.InternalMeeting import Internal_Meeting
from EventRestService.Models.OfficeTypes import Office_Types
from EventRestService.Models.TravelPlan import Travel_Plan



admin.site.register(Company_Details)
admin.site.register(External_Meetings)
admin.site.register(Internal_Meeting)
admin.site.register(Travel_Plan)
admin.site.register(Contact_alumini)
admin.site.register(Office_Types)
# admin.site.register(Assign_company)



