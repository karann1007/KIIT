from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.PlacementInfo import placement_info


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_visiting(request, format=None):
    user = request.user
    batch = request.GET.get("batch",None)
    placement_companies = placement_info.objects.filter(batch=batch,user=user)
    return Response({'response' : [{ 'placement_info_id' :e.placement_id, 'company_name' : e.comp_id , 'month' : e.month ,'school_name':e.school_id , 'profile_ctc':e.profile_ctc } for e in placement_companies]}, status=status.HTTP_200_OK)