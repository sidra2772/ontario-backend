from rest_framework import serializers
from .models import UserProfile, BusinessProfile
from django.db.models import Avg


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    user_type = serializers.CharField(source='user.user_type', read_only=True)
    country_label = serializers.CharField(source='country.common_name', read_only=True)
    timezone_label = serializers.CharField(source='timezone.timezone', read_only=True)
    country_code_label = serializers.CharField(source='country_code.calling_code', read_only=True)
    profile_status = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    business_profile = BusinessProfileSerializer(required=False, allow_null=True)
    business_profile_id = serializers.IntegerField(source='business_profile.id', write_only=True, required=False,
                                                   allow_null=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')

    def validate(self, attrs):
        if attrs.get('account_type') == 'business' and not attrs.get('business_profile'):
            raise serializers.ValidationError("Business profile is required for business account type")
        return attrs

    @staticmethod
    def get_profile_status(obj):
        return obj.profile_status()

    def get_rating(self, obj):
        return (lambda user_type: obj.servicesSupplier.aggregate(rating=Avg('service_feedback__rating'))[
                                      'rating'] or 0 if user_type == 'supplier' else
        obj.client_offer.aggregate(rating=Avg('order_feedback_supplier__rating'))[
            'rating'] or 0 if user_type == 'client' else 0)(obj.user.user_type)


class BusinessMemberUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    user_type = serializers.CharField(source='user.user_type', read_only=True)
    country_label = serializers.CharField(source='country.common_name', read_only=True)
    timezone_label = serializers.CharField(source='timezone.timezone', read_only=True)
    country_code_label = serializers.CharField(source='country_code.calling_code', read_only=True)
    profile_status = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')

    @staticmethod
    def get_profile_status(obj):
        return obj.profile_status()

    def get_rating(self, obj):
        return (lambda user_type: obj.servicesSupplier.aggregate(rating=Avg('service_feedback__rating'))[
                                      'rating'] or 0 if user_type == 'supplier' else
        obj.client_offer.aggregate(rating=Avg('order_feedback_supplier__rating'))[
            'rating'] or 0 if user_type == 'client' else 0)(obj.user.user_type)
