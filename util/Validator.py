import datetime

from Exceptions.exceptions import CustomException
from rest_framework import status

class Validator:

    @classmethod
    def validate_string(cls, input, message):
        if input is not None:
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_date(cls, date_string, message,message2):
        date_string = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        if date_string is not None:
            if datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ"):
                return
            raise CustomException(message, status.HTTP_400_BAD_REQUEST)
        raise CustomException(message2, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_time(cls, time, message):
        if time is not None:
            return
        raise CustomException(message,status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_meet(cls,open_time, close_time, meetings,message):
        otime = datetime.datetime.strptime(open_time, "%Y-%m-%dT%H:%M:%S.%fZ").time()
        ctime = datetime.datetime.strptime(close_time, "%Y-%m-%dT%H:%M:%S.%fZ").time()
        for e in meetings:
            if ((otime >= e.open_time) and (otime < e.close_time)) or ((ctime > e.open_time) and (ctime <= e.close_time)):
                raise CustomException(message, status.HTTP_400_BAD_REQUEST)
        return

    @classmethod
    def validate_company(cls, comp_id, message):
        if comp_id is not None:
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_contact(cls, contact_id, message):
        if contact_id is not None:
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_meeting_type(cls, meeting_type, message):
        if meeting_type is not None:
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_date_today(cls, meeting_date, message):
        date = datetime.datetime.strptime(meeting_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        if date >= datetime.datetime.today().date():
            return
        raise CustomException(message, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def validate_updated_meet(cls, meet_id,open_time, close_time, meetings, message):
        otime = datetime.datetime.strptime(open_time, "%Y-%m-%dT%H:%M:%S.%fZ").time()
        ctime = datetime.datetime.strptime(close_time, "%Y-%m-%dT%H:%M:%S.%fZ").time()
        for e in meetings:
            if e.meet_id == meet_id :
                continue
            if ((otime >= e.open_time) and (otime < e.close_time)) or (
                    (ctime > e.open_time) and (ctime <= e.close_time)):
                raise CustomException(message, status.HTTP_400_BAD_REQUEST)
        return

    @classmethod
    def validate_mom(cls,time, date,message):
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        today = datetime.date.today()
        ctime = datetime.datetime.now()
        if(((ctime < time)  and  (date==today)))  or  (date > today):
            raise CustomException(message, status.HTTP_400_BAD_REQUEST)
        return

