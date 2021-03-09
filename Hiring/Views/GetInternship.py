from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.InternshipInfo import internship_info



@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_internship_user(request, format=None):
    user = request.user
    comp_id = request.GET.get('comp_id', None)
    internship_details = internship_info.objects.filter(user=user,comp_id=comp_id)
    return Response({'response' : [{ 'internship_info_id' :e.internship_id, 'intern_profile_ctc' : e.intern_profile_ctc.split(' # ') if e.intern_profile_ctc is not None else e.intern_profile_ctc  ,'school_id':e.school_id.school_id,'school_name':e.school_id.school_name , 'intern_offers':e.intern_offers } for e in internship_details]}, status=status.HTTP_200_OK)