from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.ContactAlumini import Contact_alumini


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_contacts_list(request, format=None):
    comp_id = request.GET.get("comp_id",None)
    contacts  = Contact_alumini.objects.filter(comp_id=comp_id)
    return Response({'response' : [{ 'contact_id' : e.contact_id ,
                                     'contact_name' : e.contact_name ,
                                     'email' : e.email if e.email is not None else None,
                                     'mobile_number' : e.mobile_number if e.mobile_number is not None else None ,
                                     'comp_lcl_id' :  e.comp_lcl_id.comp_lcl_id if e.comp_lcl_id is not None else None,
                                     'boardline_number' : e.comp_lcl_id.phone_no if e.comp_lcl_id and e.comp_lcl_id.phone_no is not None else None,
                                     'designation': e.designation if e.designation is not None else None,
                                     'department': e.department if e.department is not None else None,
                                     'city': (e.comp_lcl_id.city if e.comp_lcl_id.city is not None else None) if e.comp_lcl_id is not None else None ,
                                     'pedigree': e.institution_name if e.institution_name is not None else None
                                     } for e in contacts]}, status=status.HTTP_200_OK)

