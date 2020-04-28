from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
	is_client = models.BooleanField(default=False)
	is_director = models.BooleanField(default=False)
	is_team = models.BooleanField(default=False)
	is_approved = models.BooleanField(default=False)


class Type(models.Model):
	
	type_name = models.CharField(max_length=50)
	added_by = models.CharField(max_length=20)

	def __str__(self):
		return self.type_name


class Ticket(models.Model):
		
	STATUS_CHOICES = (
		('pending', 'Pending'),
		('inprogress', 'Inprogress'),
		('closed', 'Closed'),
	)
	opened_by = models.ForeignKey(User, on_delete=models.PROTECT)
	opened_on = models.DateTimeField(default=timezone.now)
	closed_date = models.DateTimeField(null=True)
	office_description = models.CharField(null=True, max_length=100)
	ticket_type = models.ForeignKey(
		'type', on_delete=models.CASCADE,)
	description = models.TextField()
	status = models.CharField(max_length=10,
								choices=STATUS_CHOICES, default='pending')
	done_by = models.CharField(max_length=100)
	closed_by = models.CharField(max_length=100)

	def __str__(self):
		return str(self.id) 






