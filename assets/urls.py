from django.urls import path
from .views import (
    SubCategoriesListAPIView,
    CategoriesListAPIView,
    CountriesListAPIView,
    CountryTimeZoneListAPIView,
    CategoriesDetailAPIView,
    SubCategoriesDetailAPIView,
    CountriesDetailAPIView,
    CountryTimeZoneDetailAPIView,
    CurrencyListAPIView, CallingCodeWithNameListAPIView,
)

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view(), name='categories'),
    path('sub-categories/', SubCategoriesListAPIView.as_view(), name='sub-categories'),
    path('countries/', CountriesListAPIView.as_view(), name='countries'),
    path('country-timezone/', CountryTimeZoneListAPIView.as_view(), name='country-timezone'),
    path('categories/<str:category_slug>/', CategoriesDetailAPIView.as_view(), name='categories-detail'),
    path('sub-categories/<str:subcategory_slug>/', SubCategoriesDetailAPIView.as_view(), name='sub-categories-detail'),
    path('countries/<int:pk>/', CountriesDetailAPIView.as_view(), name='countries-detail'),
    path('country-timezone/<int:pk>/', CountryTimeZoneDetailAPIView.as_view(), name='country-timezone-detail'),
    path('currency/', CurrencyListAPIView.as_view(), name='currency'),
    path('calling-code/', CallingCodeWithNameListAPIView.as_view(), name='calling-code'),

]
