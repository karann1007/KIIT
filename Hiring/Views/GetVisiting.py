from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.CompanyDetails import Company_Details
from Hiring.Models.AssignCompany import Assign_company
from Hiring.Models.PlacementInfo import placement_info


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_visiting(request, format=None):
    user = request.user
    batch = request.GET.get("batch",None)
    assigned = Assign_company.objects.filter(user=user)
    companies = [e.comp_id for e in assigned ]
    placement_companies = placement_info.objects.filter(batch=batch,comp_id__in=companies,visit_month__isnull=False).order_by()
    return Response({'response' : [{ 'placement_info_id' :e.placement_id,'company_name':e.comp_id.company_name ,'company_id' : e.comp_id.comp_id , 'month' : e.visit_month ,'school_id':e.school_id.school_id,'school_name':e.school_id.school_name , 'profile_ctc':e.profile_ctc.split(' # ') if e.profile_ctc is not None else e.profile_ctc } for e in placement_companies]}, status=status.HTTP_200_OK)