from django.contrib import admin
from  services.models import Applications

@admin.register(Applications)
class ApplicaitonAdminSite(admin.ModelAdmin):
    list_display = ['title', 'cost_estimate', 'description']
    search_fields = ['title', 'description', 'cost_estimate']
    list_filter = ['cost_estimate']