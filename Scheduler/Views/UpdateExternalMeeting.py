from datetime import datetime
from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Scheduler.Models.ExternalMeetings import External_Meetings
from Scheduler.Models.InternalMeeting import Internal_Meeting
from Scheduler.Services.ExternalMeetingService import ExternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_external_meeting(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = External_Meetings.objects.filter(meet_id=meeting_id)
    data = request.data
    user = request.user
    date = data['meeting_date']
    meet = External_Meetings.objects.filter(meet_id=meeting_id)
    external_meetings = External_Meetings.objects.filter(meeting_date=date, user=user)
    internal_meetings = Internal_Meeting.objects.filter(meeting_date=date, user=user)
    meetings = list(chain(external_meetings, internal_meetings))
    external_meeting_service = ExternalMeetingService()
    return external_meeting_service.update_external_meeting(data,user,meetings,meet[0])