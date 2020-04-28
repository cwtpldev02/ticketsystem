from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('client/home', views.client, name = 'client_home'),
    path('team/home', views.team, name = 'team_home'),
    path('director/home', views.director, name = 'director_home'),
    path('ticket/detail<int:id>', views.ticket_details, name='ticket_detail'),
    
    
]