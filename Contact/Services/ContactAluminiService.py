from datetime import date, timedelta

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from Contact.Models.CompanyLocal import Company_Local
from Contact.Services.CompanyLocalService import CompanyLocalService
from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.ContactAlumini import Contact_alumini
from Scheduler.Models.OfficeTypes import Office_Types


class ContactAluminiService:

    def create_contact(self,data,user):
        contact = Contact_alumini()
        contact.user = user_details.objects.filter(id=user.id)[0]
        contact.comp_id = Company_Details.objects.filter(comp_id=data['comp_id'])[0]
        contact.contact_name = data['contact_name']
        referred_by_text =""
        if data.get('referred_by') is not None:
            for x in data.get('referred_by'):
                 referred_by_text += user_details.objects.filter(id=x)[0].username + " , "
            referred_by_text = referred_by_text[:-3]
        else:
            referred_by_text = data.get('referred_by')
        contact.referred_by = referred_by_text
        contact.designation = data.get('designation')
        contact.department = data.get('department')
        email_text =""
        if data.get('email') is not None:
            for x in data.get('email'):
                email_text += x + " , "
            email_text = email_text[:-3]
        else:
            email_text= data.get('email')
        contact.email = email_text

        mob_text = ""
        if data.get('mobile_number') is not None:
            for x in data.get('mobile_number'):
                mob_text += x + " , "
            mob_text = mob_text[:-3]
        else:
            mob_text = data.get('mobile_number')
        contact.mobile_number = mob_text
        contact.direct_number = data.get('direct_number')
        contact.notes = data.get('notes')
        contact.institution = data.get('institution')
        if data.get('institution') is "KIIT":
            contact.stream = data.get('stream')
            contact.school = data.get('school')
            contact.institution_name = "KIIT"
        else:
            contact.institution_name = data.get('institution_name')
            contact.stream = data.get('stream')
            contact.school = data.get('school')
        contact.yop = data.get('yop')
        contact.degree = data.get('degree')
        # contact.year = data.get('year')
        # contact.month = data.get('month')
        # delta = date.today() - date(1,data.get('month'),data.get('year'))
        # contact.total_experience = timedelta(days = delta.days)
        contact.linkedin = data.get('linkedin')
        contact.facebook = data.get('facebook')
        contact.twitter = data.get('twitter')
        contact.recruitment = data['recruitment']
        if data.get('office_id') is not None:
            if data.get('comp_lcl_id') is None:
                office_details_service= CompanyLocalService()
                contact.comp_lcl_id = office_details_service.create_company_local(data)
            else:
                contact.comp_lcl_id = Company_Local.objects.filter(comp_lcl_id=data.get('comp_lcl_id'))[0]
        else:
            contact.comp_lcl_id = None
        with transaction.atomic():
            contact.save()
            return Response({'contact_id': contact.contact_id,
                             'contact_name': contact.contact_name,
                             'referred_by': contact.referred_by.split(',') if contact.referred_by is not None else contact.referred_by ,
                             'designation': contact.designation,
                             'department': contact.department,
                             'email' : contact.email.split(',') if contact.email is not None else contact.email ,
                             'mobile_number': contact.mobile_number.split(',') if contact.mobile_number is not None else contact.mobile_number,
                             'direct_number' : contact.direct_number,
                             'notes': contact.notes,
                             'institution' : contact.institution ,
                             'institution_name' : contact.institution_name,
                             'stream': contact.stream,
                             'school': contact.school,
                             'yop': contact.yop,
                             'degree': contact.degree,
                             # 'total_experience': ((contact.total_experience.days % 365)//30 +" months and " + (contact.total_experience.days % 365) + " years"),
                             'linkedin': contact.linkedin,
                             'facebook': contact.facebook,
                             'twitter': contact.twitter,
                             'recruitment': contact.recruitment,
                             'comp_lcl_id' : contact.comp_lcl_id.comp_lcl_id if contact.comp_lcl_id is not None else None,
                             'office_id': (contact.comp_lcl_id.office_id.office_types if contact.comp_lcl_id is not None else None),
                             'comp_lcl_email': (contact.comp_lcl_id.email if contact.comp_lcl_id.email is not None else None) if contact.comp_lcl_id is not None else None,
                             'board_line_number': (contact.comp_lcl_id.phone_no if contact.comp_lcl_id.phone_no is not None else None) if contact.comp_lcl_id is not None else None,
                             'address' : (contact.comp_lcl_id.address if contact.comp_lcl_id.address is not None else None) if contact.comp_lcl_id is not None else None,
                             'city': (contact.comp_lcl_id.city if contact.comp_lcl_id.city is not None else None) if contact.comp_lcl_id is not None else None,
                             'country': (contact.comp_lcl_id.country if contact.comp_lcl_id.country is not None else None) if contact.comp_lcl_id is not None else None,
                             },status=status.HTTP_201_CREATED)

    def update_contact(self, data, contact_id,user):
        contact = Contact_alumini.objects.filter(contact_id=contact_id)[0]
        # contact.user = user_details.objects.filter(id=user.id)[0]
        # contact.comp_id = Company_Details.objects.filter(comp_id=data['comp_id'])[0]
        contact.contact_name = data.get('contact_name')
        referred_by_text = ""
        if data.get('referred_by') is not None:
            for x in data.get('referred_by'):
                referred_by_text += user_details.objects.filter(id=x)[0].username + " , "
            referred_by_text = referred_by_text[:-3]
        else:
            referred_by_text = data.get('referred_by')
        contact.referred_by = referred_by_text
        contact.designation = data.get('designation')
        contact.department = data.get('department')
        email_text = ""
        if data.get('email') is not None:
            for x in data.get('email'):
                email_text += x + " , "
            email_text = email_text[:-3]
        else:
            email_text = data.get('email')
        contact.email = email_text

        mob_text = ""
        if data.get('mobile_number') is not None:
            for x in data.get('mobile_number'):
                mob_text += x + " , "
            mob_text = mob_text[:-3]
        else:
            mob_text = data.get('mobile_number')
        contact.mobile_number = mob_text
        contact.direct_number = data.get('direct_number')
        contact.notes = data.get('notes')
        contact.institution = data.get('institution')
        if data.get('institution') is "KIIT":
            contact.stream = data.get('stream')
            contact.school = data.get('school')
            contact.institution_name = "KIIT"
        else:
            contact.institution_name = data.get('institution_name')
            contact.stream = data.get('stream')
            contact.school = data.get('school')
        contact.yop = data.get('yop')
        contact.degree = data.get('degree')
        # contact.year = data.get('year')
        contact.linkedin = data.get('linkedin')
        contact.facebook = data.get('facebook')
        contact.twitter = data.get('twitter')
        contact.recruitment = data['recruitment']
        if data.get('office_id') is not None:
            office_details_service = CompanyLocalService()
            contact.comp_lcl_id = office_details_service.create_company_local(data)
        else:
            contact.comp_lcl_id = None
        with transaction.atomic():
            contact.save()
            return Response({'contact_id': contact.contact_id,
                             'contact_name': contact.contact_name,
                             'referred_by': contact.referred_by.split(',') if contact.referred_by is not None else contact.referred_by ,
                             'designation': contact.designation,
                             'department': contact.department,
                             'email' : contact.email.split(',') if contact.email is not None else contact.email ,
                             'mobile_number': contact.mobile_number.split(',') if contact.mobile_number is not None else contact.mobile_number,
                             'direct_number' : contact.direct_number,
                             'notes': contact.notes,
                             'institution' : contact.institution ,
                             'institution_name' : contact.institution_name,
                             'stream': contact.stream,
                             'school': contact.school,
                             'yop': contact.yop,
                             'degree': contact.degree,
                             # 'year': contact.year,
                             'linkedin': contact.linkedin,
                             'facebook': contact.facebook,
                             'twitter': contact.twitter,
                             'recruitment': contact.recruitment,
                             'comp_lcl_id' : contact.comp_lcl_id.comp_lcl_id if contact.comp_lcl_id is not None else None,
                             'office_id': (contact.comp_lcl_id.office_id.office_types if contact.comp_lcl_id is not None else None),
                             'comp_lcl_email': (contact.comp_lcl_id.email if contact.comp_lcl_id.email is not None else None) if contact.comp_lcl_id is not None else None,
                             'board_line_number': (contact.comp_lcl_id.phone_no if contact.comp_lcl_id.phone_no is not None else None) if contact.comp_lcl_id is not None else None,
                             'address' : (contact.comp_lcl_id.address if contact.comp_lcl_id.address is not None else None) if contact.comp_lcl_id is not None else None,
                             'city': (contact.comp_lcl_id.city if contact.comp_lcl_id.city is not None else None) if contact.comp_lcl_id is not None else None,
                             'country': (contact.comp_lcl_id.country if contact.comp_lcl_id.country is not None else None) if contact.comp_lcl_id is not None else None,
                             }, status=status.HTTP_201_CREATED)
