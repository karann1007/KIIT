from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.PlacementStatus import Placement_Status


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_placement_status(request, format=None):
    school_id = request.GET.get("school_id", None)
    placement_status = Placement_Status.objects.filter(school_id=school_id)
    return Response({'response' : [{ 'status_id' : e.placement_status_id , 'status' : e.placement_status} for e in placement_status]}, status=status.HTTP_200_OK)