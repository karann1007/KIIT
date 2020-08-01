from datetime import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from restapi.models import Event
from util.Validator import Validator


class EventService:

    def create_event(self, data):
        event = Event()
        self.__validate_input(data)
        event.title = data['title']
        event.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        event.created_at = datetime.now().timestamp()
        event.time = data['time']
        event.modified_at = datetime.now().timestamp()
        event.location = data['location']
        event.save()
        return event.id


    def get_event_by_id(self, event_id):
        event = self.__get_by_id(event_id)
        return Response({'id': event.id,
                        'title': event.title,
                         'location': event.location,
                         'date': event.date,
                         'time': event.time})

    def __get_by_id(self, event_id):
        event_queryset = Event.objects.filter(id=event_id)
        event = event_queryset[0]
        return event

    def get_event_by_date(self, event_date):
        event_queryset = Event.objects.filter(date=event_date)
        event = event_queryset[0]
        return Response({'id': event.id,
                        'title': event.title,
                         'location': event.location,
                         'date': event.date,
                         'time': event.time})

    def update_event(self, event_id, data=None):
        event = self.__get_by_id(event_id)
        event.title = data['title']
        event.time = data['time']
        event.modified_at = datetime.now().timestamp()
        event.location = data['location']
        event.save()

    def __validate_input(self, data):
        Validator.validate_string(data['title'], "Title cannot be empty!")
        Validator.validate_string(data['location'], "Location cannot be empty!")
        Validator.validate_date(data['date'], "Format of date is incorrect")
        Validator.validate_time(data['time'], "Time field cannot be empty")


