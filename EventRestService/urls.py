from django.contrib import admin
from django.urls import path , include
# from knox import *
import KSRMLauncher
from knox import views as knox_views

from Accounts.Views.LoginAPI import LoginAPI
from Accounts.Views.RegisterAPI import RegisterAPI
from EventRestService.Views.ContactPerson import contact_person
from EventRestService.Views.CreateExternalMeeting import create_external_meeting
from EventRestService.Views.CreateInternalMeeting import create_internal_meeting
from EventRestService.Views.CreateTravelPlan import create_travel_plan
from EventRestService.Views.DeleteExternal import delete_external_meeting
from EventRestService.Views.DeleteInternal import delete_internal_meeting
from EventRestService.Views.DeleteTravel import delete_travel_plan
from EventRestService.Views.ExternalDateView import external_date_view
from EventRestService.Views.ExternalMom import external_mom
from EventRestService.Views.GetAssociates import get_associates
from EventRestService.Views.GetCompany import get_company
from EventRestService.Views.InternalDateView import internal_date_view
from EventRestService.Views.InternalMom import internal_mom
from EventRestService.Views.MeetHistory import meet_history
from EventRestService.Views.MonthTravel import month_travel
from EventRestService.Views.MonthView import month_view
from EventRestService.Views.TravelDateView import travel_date_view
from EventRestService.Views.UpdateExternalMeeting import update_external_meeting
from EventRestService.Views.UpdateInternalMeeting import update_internal_meeting
from EventRestService.Views.UpdateTravelPlan import update_travel_plan

app_name = 'EventRestService'


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),                              # register a user                             done
    path('login/', LoginAPI.as_view(), name='login'),                                       # login a user                                done
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),                        # logout user                                 done
    path('external/',create_external_meeting, name = 'external_meeting'),                   # create external meeting                     done
    path('companies/', get_company, name='get_company'),                                    # get all companies                           done
    path('contact/',contact_person, name = 'contact_person'),                               # get all contact person of that company      done
    path('associates/',get_associates, name = 'associates'),                                # get all associates(users)                   done
    path('internal/',create_internal_meeting, name = 'internal_meeting'),                   # create internal meeting                     done
    path('travelplan/', create_travel_plan, name = 'travel_plan'),                          # create travel plan                          done
    path('meethistory/', meet_history, name = 'meet_history') ,                             #  history view                               done
    path('monthview/', month_view , name = 'month_view') ,                                  #  meetings in the month                      done
    path('monthtravel/', month_travel , name = 'month_travel'),                             # travel plans in the month                   done
    path('externaldateview/', external_date_view, name='external_date_view'),               # viewing external meeting                    done
    path('internaldateview/', internal_date_view, name='internal_date_view'),               # viewing internal meeting                    done
    path('traveldateview/', travel_date_view, name='travel_date_view'),                     # viewing travel plan of that day             done
    path('updateexternal/', update_external_meeting, name='update_external_meeting'),       # update external meeting                     done
    path('updateinternal/', update_internal_meeting, name='update_internal_meeting'),       # update internal meeting                     done
    path('updatetravel/', update_travel_plan, name='update_travel_plan'),                   # update travel plan                          done
    path('externalmom/', external_mom, name='external_mom'),                                # add mom to external                         done
    path('internalmom/', internal_mom, name='internal_mom'),                                # add mom to internal                         done
    path('deleteexternal/', delete_external_meeting, name='delete_external_meeting'),       # delete external
    path('deleteinternal/', delete_internal_meeting, name='delete_internal_meeting'),       # delete internal
    path('deletetravel/', delete_travel_plan, name='delete_travel_plan'),                   # delete travel plan

]

