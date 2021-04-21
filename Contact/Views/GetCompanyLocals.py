from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Contact.Models.CompanyLocal import Company_Local
from Scheduler.Models.OfficeTypes import Office_Types


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_company_locals(request, format=None):
    comp_id = request.GET.get("comp_id",None)
    companies  = Company_Local.objects.filter(comp_id=comp_id)
    return Response({'response' : [{ 'comp_lcl_id' : e.comp_lcl_id , 'board_line_no' : e.phone_no , 'address' : e.address , 'city' : e.city , 'country' : e.country  } for e in companies]}, status=status.HTTP_200_OK)



