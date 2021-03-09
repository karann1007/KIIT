from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from EventRestService.Models.CompanyDetails import Company_Details
from Hiring.Models.PlacementInfo import placement_info
from Hiring.Models.PlacementStatus import Placement_Status
from Hiring.Models.School import School
from Hiring.Models.Stream import Stream


class PlacementDetailService:


    def create_placement_detail(self,data,user):
        self.__validate_input(data)
        placementdetail = placement_info()
        placementdetail.comp_id = Company_Details.objects.filter(comp_id = data['comp_id'])[0]
        placementdetail.school_id = School.objects.filter(school_id = data['school_id'])[0]
        placementdetail.user = user_details.objects.filter(id=user.id)[0]
        placementdetail.batch = data.get('batch')
        placementdetail.visit_month = data.get('month')
        placementdetail.placement_status_id = data.get('placement_status_id')
        profile_ctc_text = ""
        if data.get('profile_ctc') is not None:
            for e in data['profile_ctc']:
                profile_ctc_text += e + ' # '
            profile_ctc_text = profile_ctc_text[:-3]
            placementdetail.profile_ctc = profile_ctc_text
        else:
            placementdetail.profile_ctc = data.get('profile_ctc')
        placementdetail.remark = data.get('remark')
        placementdetail.offers = data.get('offers')
        with transaction.atomic():
            placementdetail.save()
            for x in data['stream_id']:
                stream = Stream.objects.filter(stream_id=x)[0]
                placementdetail.stream_id.add(stream)
        with transaction.atomic():
            placementdetail.save()
            return Response({'placement_id': placementdetail.placement_id,
                             'comp_id': placementdetail.comp_id.comp_id ,
                             'school_id' : placementdetail.school_id.school_id ,
                             'stream_id': [e.stream_id for e in placementdetail.stream_id.all()],
                             'profile_ctc': placementdetail.profile_ctc.split(' # ') if placementdetail.profile_ctc is not None else placementdetail.profile_ctc,
                             'batch': placementdetail.batch,
                             'offers': placementdetail.offers,
                             'visit_month': placementdetail.visit_month,
                             'remarks': placementdetail.remark,
                             'placement_status_id': placementdetail.placement_status_id
                             },status=status.HTTP_201_CREATED)

    def __validate_input(self, data):
        pass

    def update_placement_detail(self, data, user, placement):
        self.__validate_input(data)
        placement.comp_id = Company_Details.objects.filter(comp_id=data['comp_id'])[0]
        placement.school_id = School.objects.filter(school_id=data['school_id'])[0]
        placement.stream_id.clear()
        for x in data['stream_id']:
            stream = Stream.objects.filter(stream_id=x)[0]
            placement.stream_id.add(stream)
        placement.user = user_details.objects.filter(id=user.id)[0]
        placement.batch = data.get('batch')
        placement.visit_month = data.get('month')
        placement.placement_status_id = data.get('placement_status_id')
        profile_ctc_text = ""
        if data.get('profile_ctc') is not None:
            for e in data['profile_ctc']:
                profile_ctc_text += e + ' # '
            profile_ctc_text = profile_ctc_text[:-3]
            placement.profile_ctc = profile_ctc_text
        else:
            placement.profile_ctc = data.get('profile_ctc')
        placement.remark = data.get('remark')
        placement.offers = data.get('offers')
        with transaction.atomic():
            placement.save()
            return Response({'placement_id': placement.placement_id,
                             'comp_id': placement.comp_id.comp_id ,
                             'school_id' : placement.school_id.school_id ,
                             'stream_id': [e.stream_id for e in placement.stream_id.all()],
                             'profile_ctc': placement.profile_ctc.split(' # ') if placement.profile_ctc is not None else placement.profile_ctc,
                             'batch': placement.batch,
                             'offers': placement.offers,
                             'visit_month': placement.visit_month,
                             'remarks': placement.remark,
                             'placement_status_id': placement.placement_status_id
                             }, status=status.HTTP_201_CREATED)

