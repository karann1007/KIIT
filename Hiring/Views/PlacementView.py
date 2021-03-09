from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.PlacementInfo import placement_info


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def placement_view(request, format=None):
    user = request.user
    placement_id = request.GET.get("placement_id",None)
    placement_companies = placement_info.objects.filter(placement_id=placement_id,user=user)
    return Response({'response' : [{'placement_id': e.placement_id,
                             'comp_id': e.comp_id.comp_id ,
                             'school_id' : e.school_id.school_id ,
                             'stream_id': [x.stream_id for x in e.stream_id.all()],
                             'profile_ctc': e.profile_ctc.split('# ') if e.profile_ctc is not None else e.profile_ctc,
                             'batch': e.batch,
                             'offers': e.offers,
                             'visit_month': e.visit_month,
                             'remarks': e.remark,
                             'placement_status_id': e.placement_status_id
                             } for e in placement_companies]}, status=status.HTTP_200_OK)