from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.InternshipInfo import internship_info


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def internship_view(request, format=None):
    user = request.user
    internship_id = request.GET.get("internship_id",None)
    internships = internship_info.objects.filter(internship_id=internship_id,user=user)
    return Response({'response' : [{'internship_id': e.internship_id,
                             'comp_id': e.comp_id.comp_id,
                             'school_id': e.school_id.school_id,
                             'stream_id': [e.stream_id for e in e.stream_id.all()],
                             'intern_profile_ctc': e.intern_profile_ctc.split(' # ') if e.intern_profile_ctc is not None else e.intern_profile_ctc,
                             'intern_batch': e.intern_batch,
                             'intern_offers': e.intern_offers,
                             'start_date': e.start_date,
                             'end_date' : e.end_date ,
                             'remarks': e.intern_remark,
                             'ppo_offered' :e.ppo_offered,
                             'ppo_profile_ctc' : e.ppo_profile_ctc.split(' # ') if e.ppo_profile_ctc is not None else e.ppo_profile_ctc,
                             }for e in internships]}, status=status.HTTP_200_OK)