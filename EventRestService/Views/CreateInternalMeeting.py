from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from EventRestService.Models.ExternalMeetings import External_Meetings
from EventRestService.Models.InternalMeeting import Internal_Meeting
from EventRestService.Services.InternalMeetingService import InternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_internal_meeting(request, format=None):
    data = request.data
    user = request.user
    date = data['meeting_date']
    external_meetings = External_Meetings.objects.filter(meeting_date = date, user=user)
    internal_meetings = Internal_Meeting.objects.filter(meeting_date=date, user=user)
    meetings = list(chain(external_meetings, internal_meetings))
    internal_meeting_service = InternalMeetingService()
    return internal_meeting_service.create_internal_meeting(data,user,meetings)
