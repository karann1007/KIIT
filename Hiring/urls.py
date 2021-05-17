from django.urls import path

from Hiring.Views.GetAssignCompany import get_assigncompany
from Hiring.Views.GetCurrentHot import get_current_hot
from Hiring.Views.GetInternship import get_internship_user
from Hiring.Views.GetNextHot import get_next_hot
from Hiring.Views.GetNotConfirmed import get_not_confirmed
from Hiring.Views.GetNotVisiting import get_not_visiting
from Hiring.Views.GetPlacement import get_placement_user
from Hiring.Views.GetPlacementStatus import get_placement_status
from Hiring.Views.GetSchools import get_schools
from Hiring.Views.GetStreams import get_stream
from Hiring.Views.GetVisited import get_visited
from Hiring.Views.GetVisiting import get_visiting
from Hiring.Views.InternshipDetails import internship_details
from Hiring.Views.InternshipView import internship_view
from Hiring.Views.PlacementDetails import placement_details
from Hiring.Views.PlacementView import placement_view
from Hiring.Views.UpdateInternship import update_internship
from Hiring.Views.UpdatePlacement import update_placement
app_name = 'Hiring'
urlpatterns = [

    path('assigncompany/',get_assigncompany, name = 'assign_company'),                        #done
    path('internships/',get_internship_user, name = 'internships'),                           #done
    path('placements/',get_placement_user, name = 'placements'),                              #done
    path('schools/',get_schools, name = 'schools'),                                           #done
    path('streams/',get_stream, name = 'streams'),
    path('placement_status/',get_placement_status, name = 'placement_status'),                #done
    path('visiting/',get_visiting, name = 'visiting'),
    path('current_hot_visiting/',get_current_hot, name = 'current_hot'),
    path('next_hot_visiting/',get_next_hot, name = 'next_hot'),
    path('visited/',get_visited, name = 'visited'),
    path('not_visiting/',get_not_visiting, name = 'not_visiting'),
    path('not_confirmed/', get_not_confirmed, name='not_confirmed'),
    path('internship_details/',internship_details, name = 'internship_details'),              #Creat Internship
    path('placement_details/',placement_details, name = 'placement_details'),                 #Creat Placement
    path('internship_view/',internship_view, name = 'internship_view'),                       #done
    path('placement_view/',placement_view, name = 'placement_view'),                           #done
    path('update_internship/', update_internship, name='update_internship'),                   #done
    path('update_placement/', update_placement, name='update_placement'),                     #done

]
