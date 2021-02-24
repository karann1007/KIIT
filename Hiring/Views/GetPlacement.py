from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.PlacementInfo import placement_info
from Hiring.Models.PlacementStatus import Placement_Status
from Hiring.Models.School import School


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_placement_user(request, format=None):
    user = request.user
    comp_id = request.GET.get('comp_id',None)
    placement_details = placement_info.objects.filter(user=user,comp_id=comp_id)
    return Response({'response' : [{ 'placement_info_id' :e.placement_id, 'offers' : e.offers , 'month' : e.visit_month ,'placement_status' : e.placement_status_id.placement_status,'school_name':e.school_id.school_name, 'profile_ctc':e.profile_ctc } for e in placement_details]}, status=status.HTTP_200_OK)