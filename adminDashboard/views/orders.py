from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from dashboard.models import Orders
from adminDashboard.serializers.orders import AdminOrdersSerializer, AdminUpdateStatusSerializer, \
    AdminUpdatePaymentStatusSerializer
from dashboard.filters import OrdersFilters
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from utils.paginations.pagination import OurLimitOffsetPagination
from datetime import datetime


class AdminOrdersListView(ListAPIView):
    """ This class is used to fetch all the Orders objects """
    queryset = Orders.objects.filter(
        status__in=['in_progress', 'completed', 'rejected', 'canceled', 'pending']).select_related(
        'client', 'service', 'service__supplier').prefetch_related(
        'order_feedback').order_by('-created_at')
    pagination_class = OurLimitOffsetPagination
    serializer_class = AdminOrdersSerializer
    permission_classes = [IsAdminUser, ]
    filter_backends = (
        backend_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_class = OrdersFilters
    ordering_fields = '__all__'
    search_fields = 'service__name'


class AdminOrdersRetrieveAPIView(RetrieveAPIView):
    """ This class is used to fetch a single Orders object """
    queryset = Orders.objects.all().select_related('client', 'service', 'service__supplier').prefetch_related(
        'order_feedback')
    serializer_class = AdminOrdersSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'order_number'
    lookup_url_kwarg = 'order_number'


class AdminUpdatePaymentStatusAPIView(UpdateAPIView):
    """ This class is used to update the payment status of the order """
    queryset = Orders.objects.all()
    serializer_class = AdminUpdatePaymentStatusSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'order_number'
    lookup_url_kwarg = 'order_number'


class AdminUpdateStatusAPIView(UpdateAPIView):
    """ This class is used to update the status of the order """
    queryset = Orders.objects.all()
    serializer_class = AdminUpdateStatusSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'order_number'
    lookup_url_kwarg = 'order_number'

    def perform_update(self, serializer):
        if serializer.validated_data.get('status', None) == 'completed':
            serializer.save(completed_date=datetime.now())
        else:
            serializer.save()
