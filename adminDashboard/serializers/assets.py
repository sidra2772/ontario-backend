""" This package contains all the serializers for the admin dashboard. """
from assets.models import Categories, SubCategories
from rest_framework import serializers


class AdminCategoriesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the category. """

    class Meta:
        model = Categories
        fields = ['id', 'name', 'image', 'category_slug', 'index', 'created_at', 'updated_at']
        read_only_fields = ['id', 'category_slug', 'created_at', 'updated_at']


class AdminSubCategoriesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the sub category. """

    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'image', 'subcategory_slug', 'category', 'created_at', 'updated_at']
        read_only_fields = ['subcategory_slug', 'created_at', 'updated_at']
