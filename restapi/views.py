from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from restapi.service import EventService


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_event(request, format=None):
    data = request.data
    event_service = EventService()
    event_id = event_service.create_event(data)
    return event_service.get_event_by_id(event_id)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def event_fetch_id(request, format=None):
    event_id = request.GET.get('id')
    event_service = EventService()
    return event_service.get_event_by_id(event_id)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def filter_event(request, format=None):
    event_date = request.GET.get('date')
    event_service = EventService()
    return event_service.get_event_by_date(event_date)


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_event(request, format=None):
    event_id = request.GET.get('id')
    data = request.data
    event_service = EventService()
    event_service.update_event(event_id, data)
    return Response({'response': True})



@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_event(request, format=None):
    pass