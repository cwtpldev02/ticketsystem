from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from ticketing.models import User


from ticketing.models import User, Ticket

class ClientSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_client = True
		user.is_approved = False

		if commit:
			user.save()
		return user

class TeamSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_team = True
		user.is_approved = False

		if commit:
			user.save()
		return user

class DirectorSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_director = True
		user.is_approved = False

		if commit:
			user.save()
		return user

class TicketCreateForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ['ticket_type', 'description', 'office_description', ]



