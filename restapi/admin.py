from django.contrib import admin

# Register your models here.
from restapi.models import *

admin.site.register(Event)
admin.site.register(UserDetails)
admin.site.register(CompanyDetails)
admin.site.register(ExternalMeetings)
admin.site.register(InternalMeeting)
admin.site.register(TravelPlan)
admin.site.register(ContactAlumni)



