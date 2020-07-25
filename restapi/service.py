from datetime import datetime

from rest_framework.response import Response

from restapi.models import Event


class EventService:

    def create_event(self, data):
        event = Event()
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

