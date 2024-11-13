from datetime import date
from django.conf import settings
from rest_framework import status
from django.db import transaction
from core.models import UserActivation
from rest_framework import permissions
from core.models import UserActivation
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from utils.threads.email_thread import send_mail
from core.serializers import CreateUserSerializer, CreateBusinessUserSerializer
from core.utils.reset_email_token_util import reset_email_token
from userprofile.serializers import UserProfileSerializer, BusinessProfileSerializer, \
    BusinessMemberUserProfileSerializer
from core.utils import check_business_email_valid, create_random_password

User = get_user_model()
email = settings.EMAIL_HOST_USER
react_domain = settings.REACT_DOMAIN
domain = settings.DOMAIN


class RegistrationView(APIView):
    """Register and login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            profile = serializer.validated_data.pop('profile', None)

            serializer.save()
            if profile:

                profile_serializer = UserProfileSerializer(data=profile)
                profile_serializer.is_valid(raise_exception=True)
                if profile_serializer.validated_data.get('user_type') != 'client':
                    business_profile = profile_serializer.validated_data.pop('business_profile', None)
                    if not business_profile:
                        return Response({
                            "message": "Business profile is required"
                        }, status=status.HTTP_400_BAD_REQUEST)
                    if business_profile:
                        business_profile_serializer = BusinessProfileSerializer(data=business_profile)
                        business_profile_serializer.is_valid(raise_exception=True)
                        business_domain = business_profile_serializer.validated_data.get('business_domain', None)
                        check_business_email_valid(serializer.instance.email, business_domain)
                        business_profile_serializer.save()
                        profile_serializer.save(user=serializer.instance,
                                                business_profile=business_profile_serializer.instance)
                profile_serializer.save(
                    user=serializer.instance)

            instance = serializer.instance
            secret_key = reset_email_token(50)

            user_activation, _ = UserActivation.objects.get_or_create(
                user=instance)
            user_activation.otp = secret_key
            user_activation.is_expired = False
            user_activation.activated = False
            user_activation.save()

            key = {
                'username': instance.username,
                'otp': None, 'button': react_domain + '/auth/account-verified/' + secret_key,
                'year': date.today().year
            }

            subject = "Verify Your Account"
            template_name = "auth/new_userRegister.html"
            recipient = [request.data['email']]

            send_mail(subject=subject, html_content=template_name,
                      recipient_list=recipient, key=key)

            return Response({
                "message": "User created successfully. Check your email for verification"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


class RegisterBusinessMemberView(APIView):
    """Register and login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateBusinessUserSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            company_email = request.data['email'].split('@')[1]
            if User.objects.filter(email__contains=company_email).count() >= 25:
                return Response({"message": 'Please purchase additional licenses for $25.'},
                                status=status.HTTP_400_BAD_REQUEST)
            password = create_random_password()
            data = request.data.copy()
            data['password'] = password
            serializer = CreateBusinessUserSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            profile = serializer.validated_data.pop('profile', None)

            serializer.save()
            if profile:
                member_profile = profile.pop('business_profile', None)
                profile_serializer = BusinessMemberUserProfileSerializer(data=profile)
                profile_serializer.is_valid(raise_exception=True)
                business_domain = member_profile.business_domain
                check_business_email_valid(serializer.instance.email, business_domain)
                profile_serializer.save(
                    user=serializer.instance, business_profile=member_profile)
            instance = serializer.instance
            secret_key = reset_email_token(50)

            user_activation, _ = UserActivation.objects.get_or_create(
                user=instance)
            user_activation.otp = secret_key
            user_activation.is_expired = False
            user_activation.activated = False
            user_activation.save()

            key = {
                'username': instance.username,
                'otp': None, 'button': react_domain + '/auth/account-verified/' + secret_key,
                'year': date.today().year,
                "email": instance.email,
                "password": password
            }

            subject = "Verify Your Account"
            template_name = "auth/new_userRegister.html"
            recipient = [request.data['email']]

            send_mail(subject=subject, html_content=template_name,
                      recipient_list=recipient, key=key)

            return Response({
                "message": "User created successfully. Check your email for verification"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
