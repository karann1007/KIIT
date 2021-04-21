from datetime import datetime
from itertools import chain

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.ExternalMeetings import External_Meetings
from Scheduler.Models.InternalMeeting import Internal_Meeting

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def month_view(request, format=None):
    month = request.GET.get("month",None)
    year = request.GET.get("year", None)
    external_meetings = External_Meetings.objects.filter(user = request.user, meeting_date__year= year, meeting_date__month= month)
    internal_meetings = Internal_Meeting.objects.filter(user=request.user, meeting_date__year=year, meeting_date__month=month)
    meetings = list(chain(external_meetings, internal_meetings))
    return Response({'response' : [{ 'Id': e.meet_id,
                             'Subject': e.title,
                             'StartTime': e.open_time ,
                             'EndTime': e.close_time,
                             'meeting_type' : e.meeting_type ,
                             'notes': e.agenda, } for e in meetings]}, status=status.HTTP_200_OK)