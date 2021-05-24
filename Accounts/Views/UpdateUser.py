from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Accounts.Models.UserDetails import user_details
from Accounts.Serializer.UserDetailService import UserDetailService
from util.Validator import Validator


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_user(request, format=None,):
    Validator.validate_superuser(request.user , "Cannot Access")
    data = request.data
    # user = request.user
    user_id = request.GET.get('user_id', None)
    user = user_details.objects.filter(id=user_id)[0]
    # if user.usertype == 'Admin':
    user_detail_service = UserDetailService()
    return user_detail_service.update_user(data,user)

