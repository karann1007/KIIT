from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.ContactAlumini import Contact_alumini
from Scheduler.Models.ExternalMeetings import External_Meetings
from util.Validator import Validator


class ExternalMeetingService:

    def create_external_meeting(self,data,user,meetings):
        self.__validate_input(data,meetings)
        meet = External_Meetings()
        meet.title = data['title']
        meet.meeting_date = datetime.strptime(data['meeting_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        meet.meeting_type = data['meeting_type']
        meet.open_time = datetime.strptime(data['open_time'], "%Y-%m-%dT%H:%M:%S.%fZ").time()
        meet.close_time = datetime.strptime(data['close_time'], "%Y-%m-%dT%H:%M:%S.%fZ").time()
        assigned_to_text = ""
        for e in data['assigned_to']:
            username = user_details.objects.get(id = e).username
            assigned_to_text += username + " , "
        assigned_to_text = assigned_to_text[:-3]
        meet.assigned_to = assigned_to_text
        meet.reference = data.get('reference')
        meet.agenda = data.get('agenda')
        meet.comp_id = Company_Details.objects.get(comp_id=data['comp_id'])
        meet.user_id = user.id
        meet.contact_id = Contact_alumini.objects.get(contact_id=data['contact_id'])
        with transaction.atomic():
            meet.save()
            return Response({'meet_id': meet.meet_id,
                             'title': meet.title,
                             'open_time': meet.open_time ,
                             'close_time': meet.close_time,
                             'meeting_date': meet.meeting_date,
                             'meeting_type' : meet.meeting_type ,
                             'notes': meet.agenda,
                             'company_name' : meet.comp_id.company_name,
                             'contact_name': meet.contact_id.contact_name,
                             'username' : user.username ,
                             'assigned_to' : meet.assigned_to
                             },status=status.HTTP_201_CREATED)

    def update_external_meeting(self, data, user, meetings,meet):
        self.__validate_updated_input(data, meetings,meet.meet_id)
        meet.title = data['title']
        meet.meeting_date = datetime.strptime(data['meeting_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        meet.meeting_type = data['meeting_type']
        meet.open_time = datetime.strptime(data['open_time'], "%Y-%m-%dT%H:%M:%S.%fZ").time()
        meet.close_time = datetime.strptime(data['close_time'], "%Y-%m-%dT%H:%M:%S.%fZ").time()
        assigned_to_text = ""
        for e in data['assigned_to']:
            username = user_details.objects.get(id=e).username
            assigned_to_text += username + " , "
        assigned_to_text = assigned_to_text[:-3]
        meet.assigned_to = assigned_to_text
        meet.reference = data.get('reference')
        meet.agenda = data.get('agenda')
        meet.comp_id = Company_Details.objects.get(comp_id=data['comp_id'])
        meet.user_id = user.id
        meet.contact_id = Contact_alumini.objects.get(contact_id=data['contact_id'])
        with transaction.atomic():
            meet.save()
            return Response({'meet_id': meet.meet_id,
                             'title': meet.title,
                             'open_time': meet.open_time ,
                             'close_time': meet.close_time,
                             'meeting_date': meet.meeting_date,
                             'meeting_type' : meet.meeting_type ,
                             'notes': meet.agenda,
                             'company_name' : meet.comp_id.company_name,
                             'contact_name': meet.contact_id.contact_name,
                             'username' : user.username ,
                             'assigned_to' : meet.assigned_to
                             }, status=status.HTTP_201_CREATED)


    def __validate_input(self, data,meetings):
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('meeting_date'), "Format of date is incorrect", "Date cannot be empty")
        Validator.validate_time(data.get('open_time'), "Time field cannot be empty")
        Validator.validate_time(data.get('close_time'), "Time field cannot be empty")
        Validator.validate_date_today(data.get('meeting_date'), "Date cannot be from past")
        Validator.validate_meeting_type(data.get('meeting_type'), "Meeting Type cannot be empty")
        Validator.validate_meet(data['open_time'], data['close_time'], meetings, "Time slot already booked")

        Validator.validate_company(data.get('comp_id'), "Please select a company")
        Validator.validate_contact(data.get('contact_id'), "Please select a person to contact")
        # Validator.validate_company(data.get('agenda'), "Please select a company")

    def __validate_updated_input(self, data,meetings,meet_id):
        # Validator.validate_update(data.get('meeting_date'),data.get('open_time'),"Meeting cannot be updated")
        Validator.validate_string(data.get('title'), "Title cannot be empty!")
        Validator.validate_date(data.get('meeting_date'), "Format of date is incorrect", "Date cannot be empty")
        Validator.validate_time(data.get('open_time'), "Time field cannot be empty")
        Validator.validate_time(data.get('close_time'), "Time field cannot be empty")
        Validator.validate_date_today(data.get('meeting_date'), "Date cannot be from past")
        Validator.validate_meeting_type(data.get('meeting_type'), "Meeting Type cannot be empty")
        Validator.validate_updated_meet(meet_id,data['open_time'], data['close_time'], meetings, "Time slot already booked")
        # Validator.validate_meet(data['open_time'], data['close_time'], meetings, "Time slot already booked")
        Validator.validate_company(data.get('comp_id'), "Please select a company")
        Validator.validate_contact(data.get('contact_id'), "Please select a person to contact")

    def add_mom(self, data, meet):
        Validator.validate_mom(meet.close_time,meet.meeting_date, "Minutes of meeting cannot be added")
        meet.description = data['description']
        with transaction.atomic():
            meet.save()
            return Response({'minutes of meeting': meet.description
                             }, status=status.HTTP_201_CREATED)
