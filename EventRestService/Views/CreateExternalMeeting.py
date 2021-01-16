from datetime import datetime
from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from EventRestService.Models.ExternalMeetings import External_Meetings
from EventRestService.Models.InternalMeeting import Internal_Meeting
from EventRestService.Services.ExternalMeetingService import ExternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_external_meeting(request, format=None):
    data = request.data
    user = request.user
    date = datetime.strptime(data['meeting_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime('%Y-%m-%d')
    external_meetings = External_Meetings.objects.filter(meeting_date=date, user=user)
    internal_meetings = Internal_Meeting.objects.filter(meeting_date=date, user=user)
    meetings = list(chain(external_meetings, internal_meetings))
    external_meeting_service = ExternalMeetingService()
    return external_meeting_service.create_external_meeting(data,user,meetings)