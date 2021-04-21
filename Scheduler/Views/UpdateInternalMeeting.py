from datetime import datetime
from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Scheduler.Models.ExternalMeetings import External_Meetings
from Scheduler.Models.InternalMeeting import Internal_Meeting
from Scheduler.Services.InternalMeetingService import InternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_internal_meeting(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = Internal_Meeting.objects.filter(meet_id=meeting_id)
    data = request.data
    user = request.user
    date = data['meeting_date']
    external_meetings = External_Meetings.objects.filter(meeting_date=date, user=user)
    internal_meetings = Internal_Meeting.objects.filter(meeting_date=date, user=user)
    meetings = list(chain(external_meetings, internal_meetings))
    internal_meeting_service = InternalMeetingService()
    return internal_meeting_service.update_internal_meeting(data,user,meetings,meet[0])