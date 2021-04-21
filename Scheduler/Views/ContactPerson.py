from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.ContactAlumini import Contact_alumini


@api_view(['GET'])                                            # get persons by their company
@renderer_classes([JSONRenderer])
def contact_person(request,format=None):
    comp_id = request.GET.get("comp_id",None)
    persons = Contact_alumini.objects.filter(comp=int(comp_id))
    return Response({'response' : [{ 'contact_name' : e.contact_name , 'contact_id' : e.contact_id} for e in persons]}, status=status.HTTP_200_OK)