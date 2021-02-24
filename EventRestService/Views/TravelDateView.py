from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from EventRestService.Models.TravelPlan import Travel_Plan


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def travel_date_view(request, format=None):
    travel_id = request.GET.get("id",None)
    travels = Travel_Plan.objects.filter(tr_id=travel_id)
    return Response({'response' : [{'meet_id': e.tr_id,
                             'title': e.title,
                             'travel_from': e.travel_from,
                             'travel_to': e.travel_to,
                             'travel_date': e.travel_date,
                             'return_date': e.return_date ,
                             'notes': e.purpose
                             } for e in travels]}, status=status.HTTP_200_OK)
