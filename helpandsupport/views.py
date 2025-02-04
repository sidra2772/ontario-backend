from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from utils.paginations import OurLimitOffsetPagination
from .models import Report, ReportImage
from .serializers import ReportSerializer, CreateReportSerializer, NewsLetterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import DestroyAPIView, CreateAPIView
from userprofile.models import UserProfile
from notification.utils import send_notification, create_notification_object_apis


class NewsLetterAPIView(CreateAPIView):
    queryset = NewsLetterSerializer.Meta.model.objects.all()
    serializer_class = NewsLetterSerializer
    permission_classes = [AllowAny]


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all().prefetch_related('report_images').select_related(
        'order',
        'reporter',
        'receiver'
    )
    serializer_class = ReportSerializer
    pagination_class = OurLimitOffsetPagination
    permission_classes = [AllowAny]

    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['subject', 'description']
    filterset_fields = ['status', 'created_at', 'updated_at', 'reporter', 'receiver', 'order']
    ordering_fields = ['created_at', 'updated_at', 'status', 'subject']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateReportSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        images = serializer.validated_data.pop('report_images', None)
        order = serializer.validated_data.pop('order_id', None)

        if serializer.validated_data.get(
                'subject') == 'order_report' and not order and not self.request.user.is_authenticated:
            raise Exception({"error": 'You are not allowed to create order report'})
        if order:
            if self.request.user.is_authenticated:
                serializer.save(reporter=self.request.user.profile, order=order)
        if images:
            report = serializer.save()
            for image in images:
                ReportImage.objects.create(report=report, **image)

        serializer.save()
        admin_user_profiles = UserProfile.objects.filter(user__is_staff=True, user__is_superuser=True,
                                                         user__is_active=True,
                                                         user__is_admin=True, user__user_type='admin')
        if admin_user_profiles.exists():

            for admin_user_profile in admin_user_profiles:
                send_notification_object = create_notification_object_apis(
                    notification_type='Report',
                    sender=admin_user_profile.user,
                    receiver=admin_user_profile.user,
                    report=serializer.instance,
                    plain_text='Has submitted a report',
                    description=serializer.instance.description,
                    heading=serializer.instance.subject, )
                send_notification(send_notification_object)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(reporter=self.request.user.profile)
        return self.queryset.none()

    def perform_update(self, serializer):
        images = serializer.validated_data.pop('report_images', None)
        status = (serializer.validated_data.pop('status', None))
        order = serializer.validated_data.pop('order_id', None)
        if order:
            raise Exception({"error": 'You are not allowed to change the order'})
        if status:
            raise Exception({"error": 'You are not allowed to change the status'})
        report = serializer.save()
        if images:
            for image in images:
                ReportImage.objects.create(report=report, **image)


class ReportImageDeleteAPIView(DestroyAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(report__reporter=self.request.user.profile)
        return self.queryset.none()
