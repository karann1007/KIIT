from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from EventRestService.Models.ExternalMeetings import External_Meetings
from util.Validator import Validator


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def meet_history(request,format=None):                                   # get history of meeting
    user = request.user
    Validator.validate_company(request.GET.get("comp",None), "Please select a company")
    Validator.validate_contact(request.GET.get("contact",None), "Please select a person to contact")
    meetings = External_Meetings.objects.filter(comp_id=request.GET.get("comp", None), contact_id = request.GET.get("contact", None), user = user)
    return Response({'response' : [{ 'open_time': datetime.strptime(e.open_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ') ,
                                    'close_time': datetime.strptime(e.close_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                                    'meeting_date': datetime.strptime(e.meeting_date, "%Y-%m-%d").date().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                                     'description' : e.agenda,
                                     'minutes_of_meeting' : e.description} for e in meetings]}, status=status.HTTP_200_OK)