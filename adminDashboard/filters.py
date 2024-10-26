from django_filters import rest_framework as filters
from services.models import Services
from userprofile.models import UserProfile


class ServicesFilter(filters.FilterSet):
    min_price = filters.NumberFilter(
        field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(
        field_name="price", lookup_expr='lte')

    class Meta:
        model = Services
        fields = [
            'sub_category', 'sub_category__category',
            'supplier', 'currency', 'is_active',
            'service_status', 'min_price', 'max_price',
            'sub_category__category__category_slug',
            'sub_category__subcategory_slug', 'service_slug'
        ]


class UserProfileFilter(filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = [
            'user', 'user__user_type', 'user__is_active',
            'user__is_staff', 'user__is_superuser', 'user__email',
        ]
