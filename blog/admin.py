from django.contrib import admin
from . models import BlogPost, Events, EventBookings

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Events)
admin.site.register(EventBookings)