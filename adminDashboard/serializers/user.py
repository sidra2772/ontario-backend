""" This module contains the serializers for the user model."""
from rest_framework import serializers
from django.db.models import Avg
from django.contrib.auth import get_user_model
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer

User = get_user_model()


class CreateAdminUserSerializer(serializers.ModelSerializer):
    """ Serializer for creating an admin user."""
    profile = UserProfileSerializer()

    class Meta:
        """ Metaclass for the CreateAdminUserSerializer."""
        # pylint: disable=too-few-public-methods
        model = User
        fields = ['email', 'username', 'password', 'profile', ]
        extra_kwargs = {'password': {'write_only': True},

                        }

    def create(self, validated_data):
        """ Method to create an admin user."""
        user = User.objects.create_superuser(**validated_data)
        return user


class AllAdminUserSerializer(serializers.ModelSerializer):
    """ Serializer for all admin users."""
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    user_type = serializers.CharField(source='user.user_type', read_only=True)
    country_label = serializers.CharField(source='country.common_name', read_only=True)
    timezone_label = serializers.CharField(source='timezone.timezone', read_only=True)
    country_code_label = serializers.CharField(source='country_code.calling_code', read_only=True)
    profile_status = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)

    class Meta:
        """ Metaclass for the AllAdminUserSerializer."""
        # pylint: disable=too-few-public-methods
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('user',)

    @staticmethod
    def get_profile_status(obj):
        """ Method to get the profile status."""
        return obj.profile_status()

    def get_rating(self, obj):
        """ Method to get the rating."""
        return (lambda user_type: obj.servicesSupplier.aggregate(rating=Avg('service_feedback__rating'))[
                                      'rating'] or 0 if user_type == 'supplier' else
        obj.client_offer.aggregate(rating=Avg('order_feedback_supplier__rating'))[
            'rating'] or 0 if user_type == 'client' else 0)(obj.user.user_type)


class AllUsersSerializer(serializers.ModelSerializer):
    """ Serializer for all users."""
    username = serializers.CharField(source='user.username', read_only=True)
    user_is_active = serializers.BooleanField(source='user.is_active', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    user_type = serializers.CharField(source='user.user_type', read_only=True)
    country_label = serializers.CharField(source='country.common_name', read_only=True)
    timezone_label = serializers.CharField(source='timezone.timezone', read_only=True)
    country_code_label = serializers.CharField(source='country_code.calling_code', read_only=True)
    profile_status = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        # pylint: disable=too-few-public-methods
        """ Metaclass for the AllUsersSerializer."""
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('user',)

    @staticmethod
    def get_profile_status(obj):
        """ Method to get the profile status."""
        return obj.profile_status()

    def get_rating(self, obj):
        """ Method to get the rating."""
        return (lambda user_type: obj.servicesSupplier.aggregate(rating=Avg('service_feedback__rating'))[
                                      'rating'] or 0 if user_type == 'supplier' else
        obj.client_offer.aggregate(rating=Avg('order_feedback_supplier__rating'))[
            'rating'] or 0 if user_type == 'client' else 0)(obj.user.user_type)
