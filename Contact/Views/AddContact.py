from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Contact.Services.ContactAluminiService import ContactAluminiService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_contact(request, format=None):
    data = request.data
    user = request.user
    contact_alumini_service = ContactAluminiService()
    return contact_alumini_service.create_contact(data, user)