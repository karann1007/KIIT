from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.ExternalMeetings import External_Meetings

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def external_date_view(request, format=None):
    meeting_id = request.GET.get("id",None)
    meetings = External_Meetings.objects.filter(meet_id=meeting_id)
    return Response({'response' : [{'meet_id': e.meet_id,
                             'title': e.title,
                             'open_time': datetime.strptime(e.open_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ') ,
                             'close_time': datetime.strptime(e.close_time, "%H:%M").time().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                             'meeting_date': datetime.strptime(e.meeting_date, "%Y-%m-%d").date().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                             'meeting_type' : e.meeting_type ,
                             'notes': e.agenda,
                             'company_name' : e.comp_id,
                             'contact_name': e.contact_id,
                             'assigned_to' : e.assigned_to ,
                             'reference' : e.reference
                             } for e in meetings]}, status=status.HTTP_200_OK)
