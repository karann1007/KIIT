from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from EventRestService.Models.InternalMeeting import Internal_Meeting

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def internal_date_view(request, format=None):
    meeting_id = request.GET.get("id", None)
    meetings = Internal_Meeting.objects.filter(meet_id=meeting_id)
    return Response({'response' : [{'meet_id': e.meet_id,
                             'title': e.title,
                             'open_time':e.open_time ,
                             'close_time': e.close_time,
                             'meeting_date': e.meeting_date,
                             'meeting_type' : e.meeting_type ,
                             'notes': e.agenda,
                             } for e in meetings]}, status=status.HTTP_200_OK)
