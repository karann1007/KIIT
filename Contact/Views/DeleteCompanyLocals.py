from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Contact.Models.CompanyLocal import Company_Local


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_company_locals(request, format=None):
    comp_lcl_id = request.GET.get("comp_lcl_id",None)
    companylocal = Company_Local.objects.filter(comp_lcl_id=comp_lcl_id)[0]
    companylocal.delete()
    return Response({'message': 'Company Local deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




