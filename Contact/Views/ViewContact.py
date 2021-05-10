from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.ContactAlumini import Contact_alumini


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def view_contact(request, format=None):
    contact_id = request.GET.get("contact_id",None)
    contact  = Contact_alumini.objects.filter(contact_id=contact_id)[0]
    return Response({'contact_id': contact.contact_id,
                             'contact_name': contact.contact_name,
                             'referred_by': contact.referred_by.split(',') if contact.referred_by is not None else contact.referred_by ,
                             'designation': contact.designation if contact.designation is not None else None,
                             'department': contact.department if contact.department is not None else None,
                             'email' : contact.email if contact.email is not None else None,
                             'mobile_number': contact.mobile_number if contact.mobile_number is not None else None,
                             'direct_number' : contact.direct_number if contact.direct_number is not None else None,
                             'notes': contact.notes if contact.notes is not None else None,
                             'institution' : contact.institution if contact.institution is not None else None,
                             'institution_name' : contact.institution_name if contact.institution_name is not None else None,
                             'stream': contact.stream if contact.stream is not None else None,
                             'school': contact.school if contact.school is not None else None,
                             'yop': contact.yop if contact.yop is not None else None,
                             'degree': contact.degree if contact.degree is not None else None,
                             # 'year': contact.year if contact.year is not None else None,
                             'linkedin': contact.linkedin if contact.linkedin is not None else None,
                             'facebook': contact.facebook if contact.facebook is not None else None,
                             'twitter': contact.twitter if contact.twitter is not None else None,
                             'recruitment': contact.recruitment if contact.recruitment is not None else None,
                             'comp_lcl_id' : contact.comp_lcl_id.comp_lcl_id if contact.comp_lcl_id is not None else None,
                             'office_id': contact.comp_lcl_id.office_id.office_types if contact.comp_lcl_id is not None else None,
                             'comp_lcl_email': contact.comp_lcl_id.email if (contact.comp_lcl_id and contact.comp_lcl_id.email) is not None else None,
                             'board_line_number': contact.comp_lcl_id.phone_no if (contact.comp_lcl_id and contact.comp_lcl_id.phone_no) is not None else None,
                             'address' : contact.comp_lcl_id.address if (contact.comp_lcl_id and contact.comp_lcl_id.address) is not None else None ,
                             'city': contact.comp_lcl_id.city if (contact.comp_lcl_id and contact.comp_lcl_id.city) is not None else None,
                             'country': contact.comp_lcl_id.country if (contact.comp_lcl_id and contact.comp_lcl_id.country) is not None else None,
                              }, status=status.HTTP_200_OK)


