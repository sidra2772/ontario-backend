from django_filters import rest_framework as filters
from dashboard.models import Orders


class OrdersFilters(filters.FilterSet):
    min_total_price = filters.NumberFilter(
        field_name="total_price", lookup_expr='gte')
    max_total_price = filters.NumberFilter(
        field_name="total_price", lookup_expr='lte')
    from_hiring_date = filters.DateTimeFilter(
        field_name="hiring_date", lookup_expr='gte')
    to_hiring_date = filters.DateTimeFilter(
        field_name="hiring_date", lookup_expr='lte')
    min_discount = filters.NumberFilter(
        field_name="discount", lookup_expr='gte')
    max_discount = filters.NumberFilter(
        field_name="discount", lookup_expr='lte')

    class Meta:
        model = Orders
        fields = [
            'service', 'client', 'total_price', 'hiring_date', 'discount',
            'min_total_price', 'max_total_price', 'from_hiring_date', 'to_hiring_date',
            'min_discount', 'max_discount', 'service__supplier', 'service__service_status',
            'service__sub_category',
        ]
