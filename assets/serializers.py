from rest_framework import serializers
from assets.models import Categories, SubCategories, Countries, CountryTimeZone, Currency, CallingCodeWithName


class CategoriesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the category. """

    class Meta:
        model = Categories
        fields = ['id', 'name', 'image', 'index', 'category_slug', 'created_at', 'updated_at']
        read_only_fields = ['id', 'category_slug', 'created_at', 'updated_at']


class SubCategoriesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the sub category. """

    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'image', 'category', 'subcategory_slug', 'created_at', 'updated_at']
        read_only_fields = ['id', 'subcategory_slug', 'created_at', 'updated_at']


class CountriesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the countries. """

    class Meta:
        model = Countries
        fields = ['id', 'common_name', 'official_name', 'alpha_code_2', 'alpha_code_3', 'flag_png', 'flag_svg',
                  'flag_png_file', 'flag_svg_file', 'created_at', 'updated_at']


class CountryTimeZoneSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the country timezones. """

    class Meta:
        model = CountryTimeZone
        fields = ['id', 'country', 'timezone', 'created_at', 'updated_at']


class CurrencySerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the currencies. """

    class Meta:
        model = Currency
        fields = ['id', 'name', 'code', 'created_at', 'updated_at']


class CallingCodeWithNameSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the calling code with name. """

    class Meta:
        model = CallingCodeWithName
        fields = ['id', 'name', 'calling_code', 'created_at', 'updated_at']
