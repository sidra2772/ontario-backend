from django.contrib import admin
from services.models import Services


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'service_status', 'price', 'is_active']
    search_fields = ['name', 'description', 'price']
    list_filter = ['name', 'description', 'price', 'is_active']
    list_per_page = 10
