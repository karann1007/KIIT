from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Contact.Services.SwapService import SwapService


@api_view(['POST'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def swap_contact(request, format=None):
    contact_id = request.GET.get("contact_id",None)
    comp_id = request.GET.get("comp_id", None)
    swap_service = SwapService()
    return swap_service.swap(contact_id,comp_id)

