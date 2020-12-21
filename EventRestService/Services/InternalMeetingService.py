from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from EventRestService.Models.InternalMeeting import Internal_Meeting
from util.Validator import Validator


class InternalMeetingService:

    def create_internal_meeting(self, data, user,meetings):
        self.validate_input(data,meetings)
        meet = Internal_Meeting()
        meet.title = data['title']
        meet.meeting_type = data['meeting_type']
        meet.meeting_date = data['meeting_date']
        meet.open_time = data['open_time']
        meet.close_time = data['close_time']
        meet.meeting_type = data['meeting_type']
        meet.agenda = data.get('agenda')
        meet.user_id = user.id

        with transaction.atomic():
            meet.save()
            return Response({'meet_id': meet.meet_id,
                             'title': meet.title,
                             'open_time': meet.open_time,
                             'close_time': meet.close_time,
                             'meeting_type': meet.meeting_type,
                             'meeting_date': meet.meeting_date,
                             'notes': meet.agenda},status=status.HTTP_201_CREATED)

    def validate_input(self, data,meetings):
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('meeting_date'), "Format of date is incorrect", "Date cannot be empty")
        Validator.validate_date_today(data.get('meeting_date'), "Date cannot be from past")
        Validator.validate_time(data.get('open_time'), "Time field cannot be empty")
        Validator.validate_time(data.get('close_time'), "Time field cannot be empty")
        Validator.validate_meeting_type(data.get('meeting_type'), "Meeting Type cannot be empty")
        Validator.validate_meet(data['open_time'],data['close_time'],meetings,"Time slot already booked")

    def update_internal_meeting(self, data, user, meetings,meet):
        self.validate_updated_input(data, meetings,meet.meet_id)
        meet.title = data['title']
        meet.meeting_type = data['meeting_type']
        meet.meeting_date = data['meeting_date']
        meet.open_time = data['open_time']
        meet.close_time = data['close_time']
        meet.meeting_type = data['meeting_type']
        meet.agenda = data.get('agenda')
        meet.user_id = user.id

        with transaction.atomic():
            meet.save()
            return Response({'meet_id': meet.meet_id,
                             'title': meet.title,
                             'open_time': meet.open_time,
                             'close_time': meet.close_time,
                             'meeting_type': meet.meeting_type,
                             'meeting_date': meet.meeting_date,
                             'notes': meet.agenda}, status=status.HTTP_201_CREATED)

    def validate_updated_input(self, data, meetings,meet_id):
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('meeting_date'), "Format of date is incorrect", "Date cannot be empty")
        Validator.validate_date_today(data.get('meeting_date'), "Date cannot be from past")
        Validator.validate_time(data.get('open_time'), "Time field cannot be empty")
        Validator.validate_time(data.get('close_time'), "Time field cannot be empty")
        Validator.validate_meeting_type(data.get('meeting_type'), "Meeting Type cannot be empty")
        Validator.validate_updated_meet(meet_id,data['open_time'], data['close_time'], meetings, "Time slot already booked")

    def add_mom(self, data, meet):
        Validator.validate_mom(meet.close_time,meet.meeting_date, "Minutes of meeting cannot be added")
        meet.description = data['description']
        with transaction.atomic():
            meet.save()
            return Response({'minutes of meeting': meet.description
                             }, status=status.HTTP_201_CREATED)