from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Contact.Models.CompanyLocal import Company_Local
from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.OfficeTypes import Office_Types


class CompanyLocalService:

    def create_company_local(self, data):
        company_local = Company_Local()
        company_local.comp_id = Company_Details.objects.filter(comp_id=data['comp_id'])[0]
        company_local.office_id = Office_Types.objects.filter(office_id = data['office_id'])[0]
        company_local.email = data.get('comp_lcl_email')
        company_local.phone_no = data.get('board_line_number')
        company_local.address = data.get('address')
        company_local.city = data.get('city')
        company_local.country = data.get('country')

        with transaction.atomic():
            company_local.save()
            return company_local




    def update_company_local(self, data,comp_lcl_id):
        company_local = Company_Local.objects.filter(comp_lcl_id=comp_lcl_id)[0]
        company_local.email = data.get('email')
        company_local.phone_no = data.get('board_line_number')
        company_local.address = data.get('address')
        company_local.city = data.get('city')
        company_local.country = data.get('country')
        with transaction.atomic():
            company_local.save()
            return Response({
                  'comp_lcl_id': company_local.comp_lcl_id,
                 'board_line_no': company_local.phone_no,
                 'address': company_local.address,
                 'city': company_local.city,
                 'country': company_local.country
                }, status=status.HTTP_200_OK)


