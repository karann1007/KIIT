import datetime

from exceptions.exceptions import CustomException
from rest_framework import status

class Validator:

    @classmethod
    def validate_string(cls, input, message):
        if input is not None:
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_date(cls, date_string, message):
        if datetime.datetime.strptime(date_string, '%Y-%m-%d'):
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_time(cls, time, message):
        if time is not None:
            return
        raise CustomException(message,status.HTTP_400_BAD_REQUEST)