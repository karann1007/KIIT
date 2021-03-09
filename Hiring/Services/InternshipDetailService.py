from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from EventRestService.Models import CompanyDetails
from EventRestService.Models.CompanyDetails import Company_Details
from Hiring.Models.InternshipInfo import internship_info
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream

class InternshipDetailService:


    def create_internship_detail(self,data,user):
        self.__validate_input(data)
        internshipdetail = internship_info()
        internshipdetail.comp_id = Company_Details.objects.filter(comp_id = data['comp_id'])[0]
        internshipdetail.school_id = School.objects.filter(school_id = data['school_id'])[0]
        internshipdetail.user = user_details.objects.filter(id=user.id)[0]
        internshipdetail.intern_batch = data['intern_batch']
        internshipdetail.start_date =datetime.strptime( data['start_date'],"%Y-%m-%d").date()
        internshipdetail.end_date = datetime.strptime( data['end_date'], "%Y-%m-%d").date()
        intern_profile_ctc_text = ""
        for e in data['intern_profile_ctc']:
            intern_profile_ctc_text += e + ' # '
        intern_profile_ctc_text = intern_profile_ctc_text[:-3]
        internshipdetail.intern_profile_ctc = intern_profile_ctc_text
        internshipdetail.intern_remark = data['intern_remark']
        internshipdetail.intern_offers = data['intern_offers']
        internshipdetail.ppo_offered = data['ppo_offered']
        ppo_profile_ctc_text = ""
        for e in data['ppo_profile_ctc']:
            ppo_profile_ctc_text+= e + " # "
        ppo_profile_ctc_text = ppo_profile_ctc_text[:-3]
        internshipdetail.ppo_profile_ctc = ppo_profile_ctc_text
        with transaction.atomic():
            internshipdetail.save()
            for x in data['stream_id']:
                stream = Stream.objects.filter(stream_id=x)[0]
                internshipdetail.stream_id.add(stream)
        with transaction.atomic():
            internshipdetail.save()
            return Response({'internship_id': internshipdetail.internship_id,
                             'comp_id': internshipdetail.comp_id.comp_id,
                             'school_id': internshipdetail.school_id.school_id,
                             'stream_id': [e.stream_id for e in internshipdetail.stream_id.all()],
                             'intern_profile_ctc': internshipdetail.intern_profile_ctc.split(' # '),
                             'intern_batch': internshipdetail.intern_batch,
                             'intern_offers': internshipdetail.intern_offers,
                             'start_date': internshipdetail.start_date,
                             'end_date' : internshipdetail.end_date ,
                             'remarks': internshipdetail.intern_remark,
                             'ppo_offered' :internshipdetail.ppo_offered,
                             'ppo_profile_ctc' : internshipdetail.ppo_profile_ctc.split(' # ')
                             },status=status.HTTP_201_CREATED)

    def __validate_input(self, data):
        pass

    def update_internship_detail(self, data, user, internship):
        self.__validate_input(data)
        internship.stream_id.clear()
        internship.comp_id = Company_Details.objects.filter(comp_id=data['comp_id'])[0]
        internship.school_id = School.objects.filter(school_id=data['school_id'])[0]
        internship.user = user_details.objects.filter(id=user.id)[0]
        internship.intern_batch = data['intern_batch']
        internship.start_date = data['start_date']
        internship.end_date = data['end_date']
        intern_profile_ctc_text = ""
        for e in data['intern_profile_ctc']:
            intern_profile_ctc_text += e + ' # '
        intern_profile_ctc_text = intern_profile_ctc_text[:-3]
        internship.intern_profile_ctc = intern_profile_ctc_text
        internship.intern_remark = data['intern_remark']
        internship.intern_offers = data['intern_offers']
        internship.ppo_offered = data['ppo_offered']
        ppo_profile_ctc_text = ""
        for e in data['ppo_profile_ctc']:
            ppo_profile_ctc_text += e + " # "
        ppo_profile_ctc_text = ppo_profile_ctc_text[:-3]
        internship.ppo_profile_ctc = ppo_profile_ctc_text
        for x in data['stream_id']:
            stream = Stream.objects.filter(stream_id=x)[0]
            internship.stream_id.add(stream)
        with transaction.atomic():
            internship.save()
            return Response({'internship_id': internship.internship_id,
                             'comp_id': internship.comp_id.comp_id,
                             'school_id': internship.school_id.school_id,
                             'stream_id': [e.stream_id for e in internship.stream_id.all()],
                             'intern_profile_ctc': internship.intern_profile_ctc.split(' # '),
                             'intern_batch': internship.intern_batch,
                             'intern_offers': internship.intern_offers,
                             'start_date': internship.start_date,
                             'end_date' : internship.end_date ,
                             'remarks': internship.intern_remark,
                             'ppo_offered' :internship.ppo_offered,
                             'ppo_profile_ctc' : internship.ppo_profile_ctc.split(' # ')
                             }, status=status.HTTP_201_CREATED)
