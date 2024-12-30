from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from jobs.models import (
    Jobs,JobBids
)
from .serializers import (
    JobSerializer,
    JobBidSerializer
)



class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = Jobs
    queryset = Jobs.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

class JobBidViewSet(viewsets.ModelViewSet):
    serializer_class = JobBidSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = JobBids
    queryset = JobBids.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(bidder=self.request.user.profile)