from itertools import chain

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from EventRestService.Models.TravelPlan import Travel_Plan
from EventRestService.Services.TravelPlanService import TravelPlanService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def update_travel_plan(request, format=None):
    tr_id = request.GET.get("id", None)
    plan = Travel_Plan.objects.filter(tr_id=tr_id)
    data = request.data
    user = request.user
    travel_plan_service = TravelPlanService()
    return travel_plan_service.update_travel_plan(data,user,plan[0])