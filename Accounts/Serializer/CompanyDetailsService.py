from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Scheduler.Models.CompanyDetails import Company_Details
from util.Validator import Validator


class CompanyDetailsService:

    def create_company(self, data):
        company = Company_Details()
        self.__validate_input(company,data)
        company.company_name = data['company_name']
        zone_text = ""
        for x in data['zone']:
            zone_text += x + " , "
        zone_text = zone_text[:-3]
        company.zone = zone_text
        with transaction.atomic():
            company.save()
            return Response({
                "comp_id": company.comp_id,
                "company_name": company.company_name,
                "zone": company.zone
            }, status=status.HTTP_201_CREATED)

    def __validate_input(self, company,data):
        Validator.validate_string(data.get('company_name'), "Company Name cannot be empty!")
        Validator.validate_zone(data.get('zone'), "Zone cannot be empty!")
        Validator.validate_company(company ,data.get('company_name'), "Company Name Duplicate!!")

    def update_company(self, data, company):
        self.__validate_input(company, data)
        company.company_name = data['company_name']
        zone_text = ""
        for x in data['zone']:
            zone_text += x + " , "
        zone_text = zone_text[:-3]
        company.zone = zone_text
        with transaction.atomic():
            company.save()
            return Response({
                "comp_id": company.comp_id,
                "company_name": company.company_name,
                "zone": company.zone
            }, status=status.HTTP_200_OK)

