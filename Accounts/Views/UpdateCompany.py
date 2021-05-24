from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Accounts.Serializer.CompanyDetailsService import CompanyDetailsService
from Accounts.Serializer.UserDetailService import UserDetailService
from Scheduler.Models.CompanyDetails import Company_Details
from util.Validator import Validator


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_company(request, format=None,):
    Validator.validate_superuser(request.user , "Cannot Access")
    data = request.data
    # user = request.user
    comp_id = request.GET.get('comp_id', None)
    comp = Company_Details.objects.filter(comp_id=comp_id)[0]
    # user = request.user
    # if user.usertype == 'Admin':
    company_detail_service = CompanyDetailsService()
    return company_detail_service.update_company(data,comp)

