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
    meetings = External_Meetings.objects.filter(comp=request.GET.get("comp", None), contact = request.GET.get("contact", None), user = user)
    return Response({'response' : [{ 'meeting_date' : e.meeting_date , 'open_time' : e.open_time , 'close_time' : e.close_time , 'description' : e.agenda, 'minutes_of_meeting' : e.description} for e in meetings]}, status=status.HTTP_200_OK)