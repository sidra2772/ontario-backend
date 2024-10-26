from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from assets.models import Categories, SubCategories, Countries, CountryTimeZone, Currency, CallingCodeWithName
from assets.serializers import (
    CategoriesSerializer, SubCategoriesSerializer,
    CountriesSerializer, CountryTimeZoneSerializer,
    CurrencySerializer, CallingCodeWithNameSerializer
)
from utils.paginations import OurLimitOffsetPagination
from django_filters import rest_framework as backend_filters
from rest_framework import filters
from .filters import SubCategoriesFilter


class CategoriesListAPIView(ListAPIView):
    """ This view is used to list the categories. """

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [

        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['name', ]
    ordering_fields = ['id', 'created_at', 'updated_at']


class SubCategoriesListAPIView(ListAPIView):
    """ This view is used to list the sub categories. """

    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = SubCategoriesFilter
    search_fields = ['name', ]
    ordering_fields = ['id', 'created_at', 'updated_at']


class CountriesListAPIView(ListAPIView):
    """ This view is used to list the countries. """

    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['common_name', 'official_name']
    ordering_fields = ['id', 'common_name', 'created_at', 'updated_at']


class CountryTimeZoneListAPIView(ListAPIView):
    """ This view is used to list the country timezones. """

    queryset = CountryTimeZone.objects.all()
    serializer_class = CountryTimeZoneSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['country', 'timezone']
    search_fields = ['country__common_name', 'timezone']
    ordering_fields = ['id', 'country', 'timezone', 'created_at', 'updated_at']


class CategoriesDetailAPIView(RetrieveAPIView):
    """ This view is used to retrieve the category. """

    queryset = Categories.objects.all()
    lookup_field = 'category_slug'
    lookup_url_kwarg = 'category_slug'
    serializer_class = CategoriesSerializer
    permission_classes = (AllowAny,)


class SubCategoriesDetailAPIView(RetrieveAPIView):
    """ This view is used to retrieve the sub category. """

    queryset = SubCategories.objects.all()
    lookup_field = 'subcategory_slug'
    lookup_url_kwarg = 'subcategory_slug'
    serializer_class = SubCategoriesSerializer
    permission_classes = (AllowAny,)


class CountriesDetailAPIView(RetrieveAPIView):
    """ This view is used to retrieve the country. """

    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination


class CountryTimeZoneDetailAPIView(RetrieveAPIView):
    """ This view is used to retrieve the country timezone. """

    queryset = CountryTimeZone.objects.all()
    serializer_class = CountryTimeZoneSerializer
    permission_classes = (AllowAny,)


class CurrencyListAPIView(ListAPIView):
    """ This view is used to list the currencies. """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['name', 'code']
    ordering_fields = ['id', 'name', 'code', 'created_at', 'updated_at']


class CallingCodeWithNameListAPIView(ListAPIView):
    """ This view is used to list the calling code with name. """

    queryset = CallingCodeWithName.objects.all()
    serializer_class = CallingCodeWithNameSerializer
    permission_classes = (AllowAny,)
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['name', 'calling_code']
    ordering_fields = ['id', 'name', 'calling_code', 'created_at', 'updated_at']
