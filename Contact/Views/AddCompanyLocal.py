from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Contact.Services.CompanyLocalService import CompanyLocalService
from Contact.Services.ContactAluminiService import ContactAluminiService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_company_local(request, format=None):
    data = request.data
    copany_local_service = CompanyLocalService()
    return copany_local_service.create_company_local(data)