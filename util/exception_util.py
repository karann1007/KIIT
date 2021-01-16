import json

from django.http import HttpResponse
from rest_framework import status


class ExceptionUtil:

    @classmethod
    def get_error_object(cls, message):
        error_object = {
            "message": message
        }
        return json.dumps(error_object)

    @classmethod
    def get_custom_exception_response(cls, request, exception):
        return HttpResponse(content=ExceptionUtil.get_error_object(message=exception.message),
                            status=exception.status,
                            content_type='application/json')

    @classmethod
    def get_exception_response(cls, request, exception):
        return HttpResponse(content=ExceptionUtil.get_error_object(message="Something went wrong!LOL "),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content_type='application/json')