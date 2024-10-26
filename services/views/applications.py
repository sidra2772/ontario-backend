from rest_framework import viewsets

from coresite.asgi import application
from services.models import Applications
from services.serializers import ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status
from adminDashboard.filters import ServicesFilter
from django_filters import rest_framework as backend_filters
from rest_framework import filters
from utils.paginations import OurLimitOffsetPagination
from rest_framework.permissions import AllowAny


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user.profile)

