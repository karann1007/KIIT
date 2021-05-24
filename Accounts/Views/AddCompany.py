from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Accounts.Serializer.CompanyDetailsService import CompanyDetailsService
from Accounts.Serializer.UserDetailService import UserDetailService
from util.Validator import Validator


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_company(request, format=None,):
    Validator.validate_superuser(request.user , "Cannot Access")
    data = request.data
    company_detail_service = CompanyDetailsService()
    return company_detail_service.create_company(data)

