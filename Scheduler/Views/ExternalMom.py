from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Scheduler.Models.ExternalMeetings import External_Meetings
from Scheduler.Models.InternalMeeting import Internal_Meeting
from Scheduler.Services.ExternalMeetingService import ExternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def external_mom(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = External_Meetings.objects.filter(meet_id=meeting_id)
    data = request.data
    # user = request.user
    external_meeting_service = ExternalMeetingService()
    return external_meeting_service.add_mom(data,meet[0])

