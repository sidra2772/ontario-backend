from django_filters import rest_framework as filters
from assets.models import SubCategories


class SubCategoriesFilter(filters.FilterSet):
    class Meta:
        model = SubCategories
        fields = ['category', 'name', ]
