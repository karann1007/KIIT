from django.utils.deprecation import MiddlewareMixin

from Exceptions.exceptions import CustomException
from util.exception_util import ExceptionUtil


class ExceptionHandlerMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        if isinstance(exception, CustomException):
            return ExceptionUtil.get_custom_exception_response(request, exception)
        else:
            return ExceptionUtil.get_exception_response(request, exception)