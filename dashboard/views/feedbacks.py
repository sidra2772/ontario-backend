from dashboard.models import ClientFeedback, SupplierFeedback
from dashboard.serializers import ClientFeedbackSerializer, SupplierFeedbackSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class FeedbackViewSet(viewsets.ModelViewSet):
    """ This class is used to create a view for Feedback model. """
    queryset = ClientFeedback.objects.all()
    serializer_class = ClientFeedbackSerializer
    permission_classes = [IsAuthenticated]


class SupplierFeedbackViewSet(viewsets.ModelViewSet):
    """ This class is used to create a view for Feedback model. """
    queryset = SupplierFeedback.objects.all().select_related('service__supplier', 'client')
    serializer_class = SupplierFeedbackSerializer
    permission_classes = [IsAuthenticated]
