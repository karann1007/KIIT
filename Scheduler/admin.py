from django.contrib import admin

# Register your models here.
from Hiring.Models.AssignCompany import Assign_company
from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.ContactAlumini import Contact_alumini
from Scheduler.Models.ExternalMeetings import External_Meetings
from Scheduler.Models.InternalMeeting import Internal_Meeting
from Scheduler.Models.OfficeTypes import Office_Types
from Scheduler.Models.TravelPlan import Travel_Plan



admin.site.register(Company_Details)
admin.site.register(External_Meetings)
admin.site.register(Internal_Meeting)
admin.site.register(Travel_Plan)
admin.site.register(Contact_alumini)
admin.site.register(Office_Types)
# admin.site.register(Assign_company)



