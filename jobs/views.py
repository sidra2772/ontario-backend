from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django.db.models import Exists, OuterRef
from jobs.models import (
    Jobs,JobBids
)
from .serializers import (
    JobSerializer,
    JobBidSerializer
)
from django_filters import rest_framework as backend_filters
from rest_framework import filters



class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['user']
    model = Jobs
    def get_queryset(self):
        user = self.request.user.profile  # Get the logged-in user
        return Jobs.objects.annotate(
            is_bid=Exists(
                JobBids.objects.filter(job=OuterRef('pk'), bidder=user)
            )
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

class JobBidViewSet(viewsets.ModelViewSet):
    serializer_class = JobBidSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = JobBids
    queryset = JobBids.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(bidder=self.request.user.profile)