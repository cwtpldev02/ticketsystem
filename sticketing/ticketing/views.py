from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404,HttpResponseRedirect
from .models import Ticket, User
from ticketing.forms import ClientSignUpForm, TeamSignUpForm, DirectorSignUpForm, TicketCreateForm
from django.views.generic import (CreateView)
from django.contrib.auth.decorators import login_required
from .decorators import client_required, team_required
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# def login_view(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(data=request.POST)

# 	if form.is_valid():
# 		user = form.get_user()
# 		login(request.user)
# 		if 'next' in request.POST:
# 			return redirect(request.POST.get('next'))
# 	else:
# 		form = AuthenticationForm
# 		return redirect('registration/login.html')
		
class clientSignUp(CreateView):
	model = User
	form_class = ClientSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'client'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('client_home')

class teamSignUp(CreateView):
	model = User
	form_class = TeamSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'team'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('team_home')

class directorSignUp(CreateView):
	model = User
	form_class = DirectorSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'director'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('director_home')



def home(request):
	return render(request, 'home.html')

def director(request):
	return render(request, 'director/home.html',{})
	
@login_required
@team_required
def team(request):
	tickets = Ticket.objects.all()
	return render(request, 'team/home.html',{'tickets': tickets})

@login_required
@client_required
def client(request):
	my_tickets = Ticket.objects.filter(opened_by=request.user)

	if request.method == "POST":
		form = TicketCreateForm(request.POST)
		if form.is_valid():
			TicketAdd = form.save(commit=False)
			TicketAdd.opened_by = request.user
			TicketAdd.save()
			return redirect('client_home')

	form = TicketCreateForm()
	context = {
		'form': form,
		'my_tickets': my_tickets,
		}
	return render(request, 'client/home.html', context)

@login_required
@client_required
def ticket_details(request, id):
	ticket = get_object_or_404(Ticket, pk=id)
	return render(request, 'ticket_detail.html', {'ticket': ticket})


def login_redirect(request):
	if request.user.is_authenticated():
		user_groups = request.user.groups.values_list('name', flat=True)
		if request.user.is_team:
			return HttpResponseRedirect(reverse('team_home'))
		elif "client" in user_groups:
			return HttpResponseRedirect(reverse("client_home"))
		elif "director" in user_groups:
			return HttpResponseRedirect(reverse("director_home"))



