from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from helpandsupport.models import Report
from helpandsupport.serializers import ReportSerializer
from rest_framework.permissions import IsAdminUser
from utils.paginations import OurLimitOffsetPagination
from django_filters import rest_framework as backend_filters
from rest_framework import filters


class ReportUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Report.objects.all().prefetch_related('report_images', 'report_ws_room_messages').select_related('order')
    serializer_class = ReportSerializer
    lookup_field = 'report_number'
    lookup_url_kwarg = 'report_number'
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):

        status = serializer.validated_data.pop('status', None)
        instance = self.get_object()
        if instance.status == status:
            raise Exception({"error": 'You are not allowed to change the status'})
        report = serializer.save()
        if status == 'in_progress':
            report.status = 'in_progress'
            report.save()
        return report


class ListAdminReportsAPIView(ListAPIView):
    queryset = Report.objects.all().prefetch_related('report_images', 'report_ws_room_messages').select_related('order')
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['subject', 'description']
    filterset_fields = ['status', 'created_at', 'updated_at', 'reporter', 'receiver', 'order']
    ordering_fields = ['created_at', 'updated_at', 'status', 'subject']

    def get_queryset(self):
        return self.queryset.filter()
