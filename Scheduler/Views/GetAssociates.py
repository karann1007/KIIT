from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_associates(request, format=None):
    all_users = user_details.objects.all().order_by("username")
    return Response({'response' : [{ 'username' : e.username , 'user_id' : e.id} for e in all_users]}, status=status.HTTP_200_OK)