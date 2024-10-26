from django.contrib import admin
from .models import Categories, SubCategories, Countries, CountryTimeZone, Currency, CallingCodeWithName


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('index', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'official_name', 'alpha_code_2', 'alpha_code_3')
    search_fields = ('common_name', 'official_name', 'alpha_code_2', 'alpha_code_3')
    list_filter = ('created_at', 'updated_at')


@admin.register(CountryTimeZone)
class CountryTimeZoneAdmin(admin.ModelAdmin):
    list_display = ('country', 'timezone')
    search_fields = ('country', 'timezone')
    list_filter = ('created_at', 'updated_at')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('created_at', 'updated_at')


@admin.register(CallingCodeWithName)
class CallingCodeWithNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'calling_code')
    search_fields = ('name', 'calling_code')
    list_filter = ('created_at', 'updated_at')
