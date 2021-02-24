from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from Hiring.Models.School import School


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_schools(request, format=None):
    schools = School.objects.all()
    return Response({'response' : [{ 'school_name' : e.school_name , 'school_id' : e.school_id} for e in schools]}, status=status.HTTP_200_OK)