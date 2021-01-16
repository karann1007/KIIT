from datetime import datetime
from itertools import chain

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from EventRestService.Models.ExternalMeetings import External_Meetings
from EventRestService.Models.InternalMeeting import Internal_Meeting

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def month_view(request, format=None):
    month = request.GET.get("month",None)
    year = request.GET.get("year", None)
    external_meetings = External_Meetings.objects.filter(user = request.user, meeting_date__year= year, meeting_date__month= month)
    internal_meetings = Internal_Meeting.objects.filter(user=request.user, meeting_date__year=year, meeting_date__month=month)
    meetings = list(chain(external_meetings, internal_meetings))
    return Response({'response' : [{ 'meet_id': e.meet_id,
                             'title': e.title,
                             'open_time': datetime.strptime(e.open_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ') ,
                             'close_time': datetime.strptime(e.close_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                             'meeting_date': datetime.strptime(e.meeting_date, "%Y-%m-%d").date().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                             'meeting_type' : e.meeting_type ,
                             'notes': e.agenda, } for e in meetings]}, status=status.HTTP_200_OK)