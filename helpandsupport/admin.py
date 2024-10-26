from django.contrib import admin
from .models import (
    Report,
    ReportImage,
)


class ReportImageInline(admin.TabularInline):
    model = ReportImage
    extra = 1


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'subject', 'description', 'created_at']
    search_fields = ['receiver', 'subject', 'description', 'created_at']
    list_filter = ['receiver', 'subject', 'description', 'created_at']
    inlines = [ReportImageInline]
