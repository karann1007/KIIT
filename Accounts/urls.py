from django.urls import path

from Accounts.Views.Active import active
from Accounts.Views.AddCompany import add_company
from Accounts.Views.GetUsers import get_users
from Accounts.Views.UpdateCompany import update_company
from Accounts.Views.UpdateUser import update_user

app_name = 'Accounts'
urlpatterns = [

    path('update_user/',update_user, name = 'update_user'),
    path('get_users/', get_users, name='get_users'),
    path('active/', active, name='active'),
    path('add_company/', add_company, name='add_company'),
    path('update_company/', update_company, name='update_company'),
    # path('active/', active, name='active'),

]