from django.db import models
from coresite.mixin import AbstractTimeStampModel
from django_ckeditor_5.fields import CKEditor5Field



class BlogPost(AbstractTimeStampModel):
	title = models.CharField(max_length=50)
	body = CKEditor5Field('Text', config_name='extends')
	image = models.ImageField(upload_to="blog/images/", null=True, blank=False)
	author = models.ForeignKey("userprofile.UserProfile", on_delete=models.CASCADE,null=True)
	blog_category = models.ForeignKey("assets.Categories", on_delete=models.CASCADE, related_name='blog_posts')
	short_description = models.TextField()
	def __str__(self):
		return self.title


class Events(AbstractTimeStampModel):
	title = models.CharField(max_length=255)
	thumbnail = models.ImageField(upload_to='events/thumbnails/', null=True, blank=True)
	description = CKEditor5Field('Text', config_name='extends')
	event_date = models.DateField()
	event_time = models.TimeField()
	event_location = models.CharField(max_length=255)
	event_organizer = models.CharField(max_length=255)
	organizer_contact = models.CharField(max_length=255)
	organizer_email = models.EmailField()
	organizer_website = models.URLField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Events'
		db_table = 'events'

class EventBookings(AbstractTimeStampModel):
	event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_bookings')
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	no_of_tickets = models.IntegerField()
	comment = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
	class Meta:
		verbose_name_plural = 'Event Bookings'
		db_table = 'event_bookings'