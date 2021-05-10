from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.CompanyDetails import Company_Details



@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def all_companies(request, format=None):
    user = request.user
    companies = Company_Details.objects.all()
    companies = companies.order_by('company_name')
    return Response({'response' : [{ 'company_name' :  e.company_name ,
                                     'comp_id':e.comp_id
                                     } for e in companies]}, status=status.HTTP_200_OK)