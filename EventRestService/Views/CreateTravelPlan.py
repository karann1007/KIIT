from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from EventRestService.Services.TravelPlanService import TravelPlanService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_travel_plan(request, format=None):
    data = request.data
    user = request.user
    travel_plan_service = TravelPlanService()
    return travel_plan_service.create_travel_plan(data,user)