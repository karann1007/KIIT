from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from Accounts.Serializer.UserDetailService import UserDetailService
from util.Validator import Validator


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def active(request, format=None,):
    Validator.validate_superuser(request.user , "Cannot Access")
    active = request.GET.get('status', None)
    user_id = request.GET.get('user_id', None)
    user = user_details.objects.filter(id=user_id)[0]
    user.is_active = active
    user.save()
    return Response({
                      "user_id" :user.id,
                      "is_active" : user.is_active
    }, status=status.HTTP_200_OK)

