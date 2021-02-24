from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Hiring.Services.PlacementDetailService import PlacementDetailService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def placement_details(request, format=None):
    data = request.data
    user = request.user
    placement_detail_service = PlacementDetailService()
    return placement_detail_service.create_placement_detail(data, user)