from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from EventRestService.Models.TravelPlan import Travel_Plan
from util.Validator import Validator


class TravelPlanService:

    def create_travel_plan(self, data,user):
        self.__validate_input(data)
        plan = Travel_Plan()
        plan.title = data['title']
        plan.travel_date = data['travel_date']
        plan.return_date = data['return_date']
        plan.travel_from = data['travel_from']
        plan.travel_to = data['travel_to']
        plan.purpose = data.get('purpose')
        plan.user_id = user.id
        with transaction.atomic():
            plan.save()
            return Response({'tr_id': plan.tr_id,
                             'title': plan.title,
                             'travel_date': plan.travel_date,
                             'return_date': plan.return_date,
                             'travel_from': plan.travel_from,
                             'travel_to': plan.travel_to,
                             'notes': plan.purpose
                             },status=status.HTTP_201_CREATED)

    def update_travel_plan(self, data, user,plan):
        self.__validate_input(data)
        plan.title = data['title']
        plan.travel_date = data['travel_date']
        plan.return_date = data['return_date']
        plan.travel_from = data['travel_from']
        plan.travel_to = data['travel_to']
        plan.purpose = data.get('purpose')
        plan.user_id = user.id
        with transaction.atomic():
            plan.save()
            return Response({'tr_id': plan.tr_id,
                             'title': plan.title,
                             'travel_date': plan.travel_date,
                             'return_date': plan.return_date,
                             'travel_from': plan.travel_from,
                             'travel_to': plan.travel_to,
                             'notes': plan.purpose
                             }, status=status.HTTP_201_CREATED)


    def __validate_input(self, data):
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('travel_date'), "Format of date is incorrect","Date cannot be empty")
        Validator.validate_date(data.get('return_date'), "Format of date is incorrect","Date cannot be empty")
        Validator.validate_string(data.get('travel_from'), "Location field cannot be empty")
        Validator.validate_string(data.get('travel_to'), "Location field cannot be empty")

