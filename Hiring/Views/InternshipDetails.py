from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from Hiring.Services.InternshipDetailService import InternshipDetailService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def internship_details(request, format=None):
    data = request.data
    user = request.user
    internship_detail_service = InternshipDetailService()
    return internship_detail_service.create_internship_detail(data, user)