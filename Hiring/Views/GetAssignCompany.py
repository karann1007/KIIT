from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from EventRestService.Models.CompanyDetails import Company_Details
from Hiring.Models.AssignCompany import Assign_company



@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_assigncompany(request, format=None):
    user = request.user
    companies = Assign_company.objects.filter(user=user)
    companies = companies.order_by('comp_id')
    return Response({'response' : [{ 'company_name' : Company_Details.objects.filter(comp_id = e.comp_id.comp_id)[0].company_name ,'comp_id':e.comp_id.comp_id, 'assign_id' : e.assign_id} for e in companies]}, status=status.HTTP_200_OK)