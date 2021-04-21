from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Scheduler.Models.OfficeTypes import Office_Types


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_office_types(request, format=None):
    office_types  = Office_Types.objects.all()
    return Response({'response' : [{ 'office_id' : e.office_id , 'office_type' : e.office_types} for e in office_types]}, status=status.HTTP_200_OK)