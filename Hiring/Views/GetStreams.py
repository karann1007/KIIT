from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Hiring.Models.Stream import Stream


@api_view(['GET'])                                            # get companies and their id
@renderer_classes([JSONRenderer])
def get_stream(request, format=None):
    school_id = request.GET.get("school_id", None)
    streams = Stream.objects.filter(school_id=school_id)
    return Response({'response' : [{ 'stream_name' : e.stream_name , 'stream_id' : e.stream_id} for e in streams]}, status=status.HTTP_200_OK)