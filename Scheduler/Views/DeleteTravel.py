from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


from Scheduler.Models.InternalMeeting import Internal_Meeting


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_travel_plan(request, format=None):
    travel_id = request.GET.get("id", None)
    meet = Internal_Meeting.objects.filter(tr_id=travel_id)[0]
    meet.delete()
    return Response({'message': 'Activity deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)