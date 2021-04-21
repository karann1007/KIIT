from django.urls import path

from Contact.Views.AddContact import add_contact
from Contact.Views.DeleteCompanyLocals import delete_company_locals
from Contact.Views.GetCompanyLocals import get_company_locals
from Contact.Views.GetOfficeTypes import get_office_types
from Contact.Views.UpdateCompanyLocals import update_company_locals

app_name = 'Contact'
urlpatterns = [

    path('add_contact/',add_contact, name = 'add_contact'),
    path('get_office_types/', get_office_types, name='get_office_types'),
    path('get_company_locals/', get_company_locals, name='get_company_locals'),
    path('update_company_locals/', update_company_locals, name='update_company_locals'),
    path('delete_company_locals/', delete_company_locals, name='delete_company_locals'),


]