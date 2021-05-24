from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from Accounts.Serializer.UserDetailService import UserDetailService
from util.Validator import Validator


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_users(request, format=None,):
    Validator.validate_superuser(request.user , "User not authorized to access")
    user_list = user_details.objects.all()
    return Response([{ "name" : e.name ,
                      "user_id" :e.id,
                      "email": e.email,
                      "mobile": e.mobile ,
                      "address": e.address ,
                      "zone" : e.zone.split(',') if e.zone is not None else e.zone ,
                      "usertype" : e.usertype ,
                       "username" : e.username,
                      "is_active" : e.is_active
    } for e in user_list] , status=status.HTTP_200_OK)

