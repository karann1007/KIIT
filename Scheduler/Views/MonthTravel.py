from datetime import datetime
from itertools import chain

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.TravelPlan import Travel_Plan

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def month_travel(request, format=None):
    month = request.GET.get("month",None)
    year = request.GET.get("year", None)
    travelplans = Travel_Plan.objects.filter(user = request.user, travel_date__year = year, travel_date__month = month)
    return Response({'response' : [{ 'tr_id': e.tr_id,
                             'title': e.title,
                             'travel_date': e.travel_date ,
                             'return_date': e.return_date ,
                             'travel_from': e.travel_from,
                             'travel_to': e.travel_to,
                             'notes': e.purpose,
                             'accompanied_by': e.accompanied_by } for e in travelplans]}, status=status.HTTP_200_OK)