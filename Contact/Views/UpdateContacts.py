from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Contact.Services.CompanyLocalService import CompanyLocalService
from Contact.Services.ContactAluminiService import ContactAluminiService


@api_view(['POST'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def update_contacts(request, format=None):
    data = request.data
    contact_id = request.GET.get("contact_id",None)
    contactalumini = ContactAluminiService()
    return contactalumini.update_contact(data,contact_id,request.user)




