from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


from Scheduler.Models.InternalMeeting import Internal_Meeting


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_internal_meeting(request, format=None):
    meeting_id = request.GET.get("id", None)
    meet = Internal_Meeting.objects.filter(meet_id=meeting_id)[0]
    meet.delete()
    return Response({'message': 'Activity deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)