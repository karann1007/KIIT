from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Contact.Services.CompanyLocalService import CompanyLocalService


@api_view(['POST'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def update_company_locals(request, format=None):
    data = request.data
    comp_lcl_id = request.GET.get("comp_lcl_id",None)
    companylocal = CompanyLocalService()
    return companylocal.update_company_local(data,comp_lcl_id)




