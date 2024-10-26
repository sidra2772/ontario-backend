from django.contrib import admin
from dashboard.models import Orders, ClientFeedback, SupplierFeedback


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'client', 'service', 'status', 'completed_date', 'total_price', 'payment_status',
                    'hiring_date']
    search_fields = ['order_number', ]
    list_filter = ['status', 'payment_status']
    readonly_fields = ['order_number', 'client', 'hiring_date', 'created_at', 'updated_at', 'payment_status']
    list_per_page = 10


@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ['order', 'rating', 'created_at']
    search_fields = ['order__order_number', 'order__client__user__username']
    list_filter = ['rating']
    list_per_page = 10


@admin.register(SupplierFeedback)
class SupplierFeedbackAdmin(admin.ModelAdmin):
    list_display = ['rating', 'created_at']
    search_fields = ['order__order_number', 'order__service__supplier__user__username']
    list_filter = ['rating']
    list_per_page = 10
