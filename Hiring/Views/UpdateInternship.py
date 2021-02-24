from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Hiring.Models.InternshipInfo import internship_info
from Hiring.Models.PlacementInfo import placement_info
from Hiring.Services.InternshipDetailService import InternshipDetailService
from Hiring.Services.PlacementDetailService import PlacementDetailService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_internship(request, format=None):
    data = request.data
    user = request.user
    # placement_id = request.GET.get("placement_id", None)
    internship_id = request.GET.get("internship_id", None)
    # placement = placement_info.objects.filter(user= user ,placement_id=placement_id )
    internship = internship_info.objects.filter(user= user ,internship_id=internship_id )[0]
    internship_detail_service = InternshipDetailService()
    return internship_detail_service.update_internship_detail(data, user,internship)