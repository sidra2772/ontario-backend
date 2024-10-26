from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from adminDashboard.serializers import AdminCategoriesSerializer, AdminSubCategoriesSerializer
from assets.models import Categories, SubCategories
from utils.paginations import OurLimitOffsetPagination
from django_filters import rest_framework as backend_filters
from rest_framework import filters
from assets.filters import SubCategoriesFilter
from django.utils.text import slugify


class CategoriesViewSet(viewsets.ModelViewSet):
    """ This viewSet is used to perform CRUD operations on the categories. """

    permission_classes = [IsAdminUser]
    serializer_class = AdminCategoriesSerializer
    pagination_class = OurLimitOffsetPagination
    filter_backends = [

        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['name', ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    lookup_field = 'category_slug'
    lookup_url_kwarg = 'category_slug'
    queryset = Categories.objects.all()

    def perform_create(self, serializer):
        latest_category = Categories.objects.all()
        if latest_category.exists():
            latest_category = latest_category.last()
            latest_category_id = latest_category.id + 1
        else:
            latest_category_id = 1
        category_slug = str(latest_category_id) + "-" + slugify(serializer.validated_data['name'])
        serializer.save(category_slug=category_slug)


class SubCategoriesViewSet(viewsets.ModelViewSet):
    """ This viewSet is used to perform CRUD operations on the sub categories. """

    permission_classes = [IsAdminUser]
    serializer_class = AdminSubCategoriesSerializer
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = SubCategoriesFilter
    search_fields = ['name', ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    lookup_field = 'subcategory_slug'
    lookup_url_kwarg = 'subcategory_slug'
    queryset = SubCategories.objects.all()

    def perform_create(self, serializer):
        latest_subcategory = SubCategories.objects.all()
        if latest_subcategory.exists():
            latest_subcategory = latest_subcategory.last()
            latest_subcategory_id = latest_subcategory.id + 1
        else:
            latest_subcategory_id = 1
        subcategory_slug = str(latest_subcategory_id) + "-" + slugify(serializer.validated_data['name'])
        serializer.save(subcategory_slug=subcategory_slug)
