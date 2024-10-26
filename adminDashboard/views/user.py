from datetime import date
from django.conf import settings
from rest_framework import status
from django.db import transaction
from rest_framework import permissions
from core.models import UserActivation
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from utils.threads.email_thread import send_mail
from adminDashboard.serializers import CreateAdminUserSerializer, AllAdminUserSerializer, AllUsersSerializer
from core.utils.reset_email_token_util import reset_email_token
from userprofile.serializers import UserProfileSerializer
from rest_framework.permissions import IsAdminUser
from adminDashboard.filters import UserProfileFilter
from rest_framework import filters
from utils.paginations import OurLimitOffsetPagination
from django_filters import rest_framework as backend_filters

User = get_user_model()
email = settings.EMAIL_HOST_USER
react_domain = settings.REACT_DOMAIN
domain = settings.DOMAIN


class RegistrationAdminAPIView(APIView):
    """Register and login api instant """

    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CreateAdminUserSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = CreateAdminUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = serializer.validated_data.pop('profile', None)

        serializer.save(user_type='admin')
        if profile:
            profile_serializer = UserProfileSerializer(data=profile)
            profile_serializer.is_valid(raise_exception=True)

            profile_serializer.save(
                user=serializer.instance)

        instance = serializer.instance
        secret_key = reset_email_token(50)

        user_activation, _ = UserActivation.objects.get_or_create(
            user=instance)
        user_activation.otp = secret_key
        user_activation.is_expired = True
        user_activation.activated = True
        user_activation.save()

        key = {
            'username': instance.username,
            'otp': None, 'button': None,
            'year': date.today().year
        }

        subject = "Verify Your Account"
        template_name = "auth/new_userRegister.html"
        recipient = [request.data['email']]

        send_mail(subject=subject, html_content=template_name,
                  recipient_list=recipient, key=key)

        return Response({
            "message": "User created successfully."
        }, status=status.HTTP_201_CREATED)


class AllAdminUserAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllAdminUserSerializer
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = UserProfileFilter
    search_fields = ['user__username', 'user__email']
    ordering_fields = ['id', 'user__name', 'created_at', 'updated_at']
    queryset = UserProfileSerializer.Meta.model.objects.filter(user__user_type='admin',
                                                               user__is_superuser=True).select_related('user')


class AllUsersAPIView(ListAPIView):
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,

    ]
    filterset_class = UserProfileFilter
    search_fields = ['user__username', 'user__email']
    ordering_fields = ['id', 'user__name', 'created_at', 'updated_at']
    permission_classes = [IsAdminUser]
    serializer_class = AllUsersSerializer
    queryset = UserProfileSerializer.Meta.model.objects.exclude(user__user_type="admin",
                                                                user__is_superuser=True).select_related('user')


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllAdminUserSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all().select_related('user')
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        user.is_active = not user.is_active
        user.save()
        return Response({
            "message": "User updated"}, status=status.HTTP_200_OK)
