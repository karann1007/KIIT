from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from EventRestService.Models.ExternalMeetings import External_Meetings


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_external_meeting(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = External_Meetings.objects.filter(meet_id=meeting_id)
    meet[0].delete()
    return Response({'message': 'Activity deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)