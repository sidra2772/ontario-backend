from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from userprofile.serializers import UserProfileSerializer, BusinessMemberUserProfileSerializer
import re

non_business_emails = settings.NON_BUSINESS_EMAILS

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    def validate(self, attrs):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        value = attrs['email']
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Invalid email format.")

        # Extract the domain from the email
        domain = value.split('@')[1]

        # Check if the domain is in the non-business list
        if domain in non_business_emails:
            raise serializers.ValidationError("This email domain is not allowed. Please use a business email.")
        return attrs

    class Meta:
        model = User
        fields = ['email', 'username', 'password',
                  'user_type', 'profile', ]
        extra_kwargs = {'password': {'write_only': True},

                        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ResendActivationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CreateBusinessUserSerializer(serializers.ModelSerializer):
    profile = BusinessMemberUserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'password',
                  'user_type', 'profile']
        extra_kwargs = {'password': {'write_only': True},

                        }

    def validate(self, attrs):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        value = attrs['email']
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Invalid email format.")

        # Extract the domain from the email
        domain = value.split('@')[1]

        # Check if the domain is in the non-business list
        if domain in non_business_emails:
            raise serializers.ValidationError("This email domain is not allowed. Please use a business email.")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=True)
        return user
