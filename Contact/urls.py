from django.urls import path

from Contact.Views.AddContact import add_contact
from Contact.Views.AllCompanies import all_companies
from Contact.Views.DeleteCompanyLocals import delete_company_locals
from Contact.Views.GetCompanyLocals import get_company_locals
from Contact.Views.GetContactsList import get_contacts_list
from Contact.Views.GetOfficeTypes import get_office_types
from Contact.Views.SwapContact import swap_contact
from Contact.Views.UpdateCompanyLocals import update_company_locals
from Contact.Views.UpdateContacts import update_contacts
from Contact.Views.ViewContact import view_contact

app_name = 'Contact'
urlpatterns = [

    path('add_contact/',add_contact, name = 'add_contact'),
    path('get_office_types/', get_office_types, name='get_office_types'),
    path('get_company_locals/', get_company_locals, name='get_company_locals'),
    path('update_company_locals/', update_company_locals, name='update_company_locals'),
    path('delete_company_locals/', delete_company_locals, name='delete_company_locals'),
    path('get_contacts_list/', get_contacts_list, name='get_contacts_list'),
    path('view_contact/', view_contact, name='view_contact'),
    path('update_contacts/', update_contacts, name='update_contacts'),
    path('all_companies/', all_companies, name='all_companies'),
    path('swap_contact/', swap_contact, name='swap_contact'),

]