from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Accounts.Serializer.UserDetailService import UserDetailService
from util.Validator import Validator


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def register(request, format=None,):
    Validator.validate_superuser(request.user , "Cannot Access")
    data = request.data
    user_detail_service = UserDetailService()
    return user_detail_service.create_user(data)

