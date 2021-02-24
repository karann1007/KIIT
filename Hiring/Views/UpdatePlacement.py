from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Hiring.Models.InternshipInfo import internship_info
from Hiring.Models.PlacementInfo import placement_info
from Hiring.Services.PlacementDetailService import PlacementDetailService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_placement(request, format=None):
    data = request.data
    user = request.user
    placement_id = request.GET.get("placement_id", None)
    placement = placement_info.objects.filter(user= user ,placement_id=placement_id )[0]
    placement_detail_service = PlacementDetailService()
    return placement_detail_service.update_placement_detail(data, user,placement)