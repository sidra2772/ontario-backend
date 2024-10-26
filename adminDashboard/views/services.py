from services.models import Services
from adminDashboard.serializers import AdminServicesSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from rest_framework.permissions import IsAdminUser
from adminDashboard.filters import ServicesFilter
from utils.paginations.pagination import OurLimitOffsetPagination
from django.db.models import Avg
from notification.utils import send_notification, create_notification_object_apis


class AdminServicesList(ListAPIView):
    """ This view is used to list all the services """

    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ServicesFilter
    search_fields = ['name', 'description']
    ordering_fields = '__all__'
    queryset = Services.objects.filter(
        service_status__in=['Active', 'Rejected', 'Pending', 'Inactive']).prefetch_related(
        'service_feedback').select_related(
        'supplier',
        'sub_category__category',
        'sub_category',
        'supplier__user', 'currency'
    ).annotate(
        rating=Avg('service_feedback__rating')
    )
    serializer_class = AdminServicesSerializer
    permission_classes = [IsAdminUser]


class AdminServicesRetrieveUpdate(RetrieveUpdateAPIView):
    """ This view is used to retrieve and update a service """
    queryset = Services.objects.filter(
        service_status__in=['Active', 'Rejected', 'Pending', 'Inactive']).prefetch_related(
        'service_feedback').select_related(
        'supplier',
        'sub_category__category',
        'sub_category',
        'supplier__user', 'currency'
    ).annotate(
        rating=Avg('service_feedback__rating')
    )
    serializer_class = AdminServicesSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        """ This method is used to update a service """

        instance = self.get_object()
        serializer = AdminServicesSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        notification = create_notification_object_apis(
            notification_type='Service',
            sender=request.user,
            receiver=instance.supplier.user,
            service=instance,
            heading='Update the Service',
            plain_text='Service is Updated',
            description='Service is updated successfully'
        )
        send_notification(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)
