from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from Scheduler.Models.CompanyDetails import Company_Details
from Scheduler.Models.ContactAlumini import Contact_alumini


class SwapService:

    def swap(self,contact_id,comp_id):
        Company = Company_Details.objects.filter(comp_id=comp_id)[0]
        Contact = Contact_alumini.objects.filter(contact_id=contact_id)[0]
        Contact.comp_id = Company
        Contact.comp_lcl_id = None
        with transaction.atomic():
            Contact.save()
            return Response({'message': 'Contact swapped successfully!'}, status=status.HTTP_200_OK)
