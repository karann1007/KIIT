from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from EventRestService.Models.TravelPlan import Travel_Plan
from util.Validator import Validator


class TravelPlanService:

    def create_travel_plan(self, data,user):
        self.__validate_input(data)
        plan = Travel_Plan()
        plan.title = data['title']
        plan.travel_date = datetime.strptime(data['travel_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime('%Y-%m-%d')
        plan.return_date = datetime.strptime(data['return_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime('%Y-%m-%d')
        plan.travel_from = data['travel_from']
        plan.travel_to = data['travel_to']
        plan.purpose = data.get('purpose')
        accompanied_by_text = ""
        for e in data['accompanied_by']:
            username = user_details.objects.get(id=e).username
            accompanied_by_text += username + " , "
        accompanied_by_text = accompanied_by_text[:-3]
        plan.accompanied_by = accompanied_by_text
        plan.user_id = user.id
        with transaction.atomic():
            plan.save()
            return Response({'tr_id': plan.tr_id,
                             'title': plan.title,
                             'travel_date': datetime.strptime(plan.travel_date,'%Y-%m-%d').date().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                             'return_date': datetime.strptime(plan.return_date,'%Y-%m-%d').date().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                             'travel_from': plan.travel_from,
                             'travel_to': plan.travel_to,
                             'notes': plan.purpose,
                             'accompanied_by': plan.accompanied_by
                             },status=status.HTTP_201_CREATED)

    def update_travel_plan(self, data, user,plan):
        self.__validate_input(data)
        plan.title = data['title']
        plan.travel_date = datetime.strptime(data['travel_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime('%Y-%m-%d')
        plan.return_date = datetime.strptime(data['return_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date().strftime('%Y-%m-%d')
        plan.travel_from = data['travel_from']
        plan.travel_to = data['travel_to']
        plan.purpose = data.get('purpose')
        accompanied_by_text = ""
        for e in data['accompanied_by']:
            username = user_details.objects.get(id=e).username
            accompanied_by_text += username + " , "
        accompanied_by_text = accompanied_by_text[:-3]
        plan.accompanied_by = accompanied_by_text
        plan.user_id = user.id
        with transaction.atomic():
            plan.save()
            return Response({'tr_id': plan.tr_id,
                             'title': plan.title,
                             'travel_date': datetime.strptime(plan.travel_date,'%Y-%m-%d').date().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                             'return_date': datetime.strptime(plan.return_date,'%Y-%m-%d').date().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                             'travel_from': plan.travel_from,
                             'travel_to': plan.travel_to,
                             'notes': plan.purpose,
                             'accompanied_by': plan.accompanied_by
                             }, status=status.HTTP_201_CREATED)


    def __validate_input(self, data):
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('travel_date'), "Format of date is incorrect","Date cannot be empty")
        Validator.validate_date(data.get('return_date'), "Format of date is incorrect","Date cannot be empty")
        Validator.validate_string(data.get('travel_from'), "Location field cannot be empty")
        Validator.validate_string(data.get('travel_to'), "Location field cannot be empty")

