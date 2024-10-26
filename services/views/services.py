from rest_framework import viewsets
from services.models import Services
from services.serializers import ServicesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.text import slugify
from adminDashboard.filters import ServicesFilter
from django_filters import rest_framework as backend_filters
from rest_framework import filters
from utils.paginations import OurLimitOffsetPagination
from notification.utils import send_notification, create_notification_object_apis
from django.db.models import Avg
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView


class PopularServicesViewSet(ListAPIView):
    queryset = Services.objects.all().prefetch_related(
    ).select_related(
        'supplier', 'currency',
        'sub_category',
        'sub_category__category'
    ).annotate(
        rating=Avg('service_feedback__rating')
    )
    permission_classes = [AllowAny]
    serializer_class = ServicesSerializer

    def get_queryset(self):
        return self.queryset.filter(service_status='Active').order_by('-rating')[:10]


class ServicesViewSet(viewsets.ModelViewSet):
    """ This viewSet automatically provides `list` and `detail` actions. """
    queryset = Services.objects.all().prefetch_related(
    ).select_related(
        'supplier', 'currency',
        'sub_category',
        'sub_category__category'
    ).annotate(
        rating=Avg('service_feedback__rating')
    )
    permission_classes = [AllowAny]
    serializer_class = ServicesSerializer
    lookup_url_kwarg = 'service_slug'
    lookup_field = 'service_slug'
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = ServicesFilter
    pagination_class = OurLimitOffsetPagination
    search_fields = ['name', 'description', 'price']
    ordering_fields = ['id', 'price', 'created_at', 'updated_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'supplier':
                return self.queryset.filter(supplier=self.request.user.profile)
        return self.queryset.filter(service_status='Active')

    def perform_create(self, serializer):
        """ This method is used to create a service """
        if self.request.user.user_type != 'supplier':
            return Response({'error': 'You are not allowed to create a service'}, status=status.HTTP_403_FORBIDDEN)
        latest_service = Services.objects.last()
        if latest_service:
            latest_id = latest_service.id + 1
        else:
            latest_id = 1
        serializer.save(supplier=self.request.user.profile,
                        service_slug=str(latest_id) + "-" + slugify(serializer.validated_data['name']))

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """ This method is used to update a service """

        instance = self.get_object()
        if request.user.profile.id != instance.supplier.id:
            return Response({'error': 'You are not allowed to update this service'}, status=status.HTTP_403_FORBIDDEN)
        if request.data.get('service_status', None) in ['Rejected']:
            return Response({'error': 'You are not allowed to update this service'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ServicesSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """ This method is used to delete a service """
        instance = self.get_object()
        if request.user.profile.id != instance.supplier.id:
            return Response({'error': 'You are not allowed to delete this service'}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
