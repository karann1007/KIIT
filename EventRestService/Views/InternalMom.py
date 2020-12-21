from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from EventRestService.Models.ExternalMeetings import External_Meetings
from EventRestService.Models.InternalMeeting import Internal_Meeting
from EventRestService.Services.InternalMeetingService import InternalMeetingService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def internal_mom(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = Internal_Meeting.objects.filter(meet_id=meeting_id)
    data = request.data
    # user = request.user
    internal_meeting_service = InternalMeetingService()
    return internal_meeting_service.add_mom(data,meet[0])

