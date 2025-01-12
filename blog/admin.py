from django.contrib import admin
from . models import BlogPost, Events, EventBookings

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author__user__username']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10
    date_hierarchy = 'created_at'

admin.site.register(Events)
admin.site.register(EventBookings)