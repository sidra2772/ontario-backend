from rest_framework.viewsets import ModelViewSet
from dashboard.models import Orders
from rest_framework.generics import UpdateAPIView
from dashboard.serializers.orders import OrdersSerializer, SupplierUpdatePaymentSerializer, CancelOrderSerializer
from dashboard.utils import get_order_number
import datetime
from django.db.models import Q
from dashboard.filters import OrdersFilters
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from utils.paginations.pagination import LimitOffsetPagination
from django_filters import rest_framework as backend_filters
from rest_framework.permissions import IsAuthenticated
from notification.utils import send_notification, create_notification_object_apis


class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.exclude(status__in=['withdraw', 'rejected']).prefetch_related(
        'order_feedback').select_related('client', 'service__supplier',
                                         'service').order_by('-created_at')
    serializer_class = OrdersSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = OrdersFilters
    permission_classes = [IsAuthenticated]
    search_fields = ['order_number', 'service__name', 'client__user__username']
    ordering_fields = ['order_number', 'total_price', 'hiring_date', 'discount', 'created_at', 'updated_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.method == 'UPDATE' or self.request.method == 'PATCH' or self.request.method == 'PUT':
                return Orders.objects.filter(
                    Q(client=self.request.user.profile) | Q(service__supplier=self.request.user.profile) |
                    Q(job__bidder=self.request.user.profile)| Q(job__bidder=self.request.user.profile))
            if self.request.user.user_type == 'client':
                return self.queryset.filter(client=self.request.user.profile).exclude(status='pending')
            return self.queryset.filter(Q(service__supplier=self.request.user.profile)|Q(job__bidder=self.request.user.profile)).exclude(status='pending')
        return self.queryset.none()

    def perform_create(self, serializer):

        is_custom = serializer.validated_data.get('is_custom_offer')
        client = self.request.user.profile
        if is_custom:
            client = serializer.validated_data.get('client', None)
        serializer.save(order_number=get_order_number(), hiring_date=datetime.datetime.now(), client=client)
        instance = serializer.instance
        # if not is_custom:
        #     notification = create_notification_object_apis(
        #         notification_type='Order',
        #         sender=instance.client.user,
        #         receiver=instance.service.supplier.user,
        #         order=instance,
        #         heading='Placed a order',
        #         description=f'Order is placed successfully with order number {serializer.data["order_number"]}'
        #     )
        #     send_notification(notification)
        # else:
        #     notification = create_notification_object_apis(
        #         notification_type='Chat',
        #         sender=instance.service.supplier.user,
        #         receiver=instance.client.user,
        #         order=instance,
        #         heading='Placed a custom order',
        #         description=f'Custom order is placed successfully with order number {serializer.data["order_number"]}'
        #     )
        #     send_notification(notification)

    def perform_update(self, serializer):
        instance = serializer.instance
        if instance.status in ['rejected', 'withdraw', 'completed']:
            return Response({'message': 'You can not update this order.'}, status=status.HTTP_400_BAD_REQUEST)
        if instance.status == 'in_progress' and serializer.validated_data.get('status') != 'completed':
            return Response({'message': 'You can not update status of this order.'}, status=status.HTTP_400_BAD_REQUEST)
        # if instance.status == 'pending' and serializer.validated_data.get('status') == 'in_progress':
        #     notification = create_notification_object_apis(
        #         notification_type='Order',
        #         sender=instance.client.user,
        #         receiver=instance.service.supplier.user,
        #         order=instance,
        #         heading='Update the Order status',
        #         description=f'Order {instance.order_number} is in progress.'
        #     )
        #     send_notification(notification)

        serializer.save(completed_date=datetime.datetime.now())
        # if serializer.validated_data.get('status') == 'completed':
        #     notification = create_notification_object_apis(
        #         notification_type='Order',
        #         sender=instance.client.user,
        #         receiver=instance.service.supplier.user,
        #         order=instance,
        #         heading='Update the Order status',
        #         description=f'Order {instance.order_number} is completed.'
        #     )
        #     send_notification(notification)
        # if serializer.validated_data.get('status') == 'rejected':
        #     notification = create_notification_object_apis(
        #         notification_type='Order',
        #         sender=instance.client.user,
        #         receiver=instance.service.supplier.user,
        #         order=instance,
        #         heading='Update the Order status',
        #         description=f'Order {instance.order_number} is rejected.'
        #     )
        #     send_notification(notification)


class UpdatePaymentStatusAPIView(UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = SupplierUpdatePaymentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'order_number'
    lookup_url_kwarg = 'order_number'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(Q(service__supplier=self.request.user.profile)|Q(job__bidder=self.request.user.profile))
        return self.queryset.none()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'in_progress':
            return Response({'message': 'You can not update payment status of this order.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # notification = create_notification_object_apis(
        #     notification_type='Order',
        #     sender=instance.service.supplier.user,
        #     receiver=instance.client.user,
        #     order=instance,
        #     heading='Update the Payment status',
        #     description=f'Payment status of order {instance.order_number} is updated to {request.data["payment_status"]}'
        # )
        # send_notification(notification)
        return super().update(request, *args, **kwargs)


class CancelOrderStatusAPIView(UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = CancelOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'order_number'
    lookup_url_kwarg = 'order_number'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(client=self.request.user.profile)
        return self.queryset.none()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status not in ['pending', 'in_progress']:
            return Response({'message': 'You can not cancel this order.'}, status=status.HTTP_400_BAD_REQUEST)
        notification = create_notification_object_apis(
            notification_type='Order',
            sender=instance.client.user,
            receiver=instance.service.supplier.user,
            order=instance,
            heading='Cancel the Order',
            description=f'Order {instance.order_number} is cancelled by client.'
        )
        send_notification(notification)
        return super().update(request, *args, **kwargs)
