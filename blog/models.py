from django.db import models
from coresite.mixin import AbstractTimeStampModel
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify



class BlogPost(AbstractTimeStampModel):
	title = models.CharField(max_length=255)
	body = CKEditor5Field('Text', config_name='extends')
	slug = models.SlugField(max_length=255, unique=True,editable=False)
	image = models.ImageField(upload_to="blog/images/", null=True, blank=False)
	author = models.ForeignKey("userprofile.UserProfile", on_delete=models.CASCADE,null=True)
	blog_category = models.ForeignKey("assets.Categories", on_delete=models.CASCADE, related_name='blog_posts')
	short_description = models.TextField()
	def __str__(self):
		return self.title
	def save(self, *args, **kwargs):
		"""
        Overridden save method to generate a unique slug for the blog post
        based on its title and ID.
        """
		if not self.slug:  # Generate slug only for new entries or if slug is missing
			latest_id = (
				BlogPost.objects.latest('id').id + 1
				if BlogPost.objects.exists()
				else 1
			)
			self.slug = f"{latest_id}-{slugify(self.title)}"
		super().save(*args, **kwargs)


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