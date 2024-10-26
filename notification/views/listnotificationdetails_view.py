from rest_framework.generics import ListAPIView
from notification.serializers import NotificationDetailsSerializer
from utils.paginations.pagination import OurLimitOffsetPagination
from notification.models.notification_model import NotificationDetails
import logging


class NotificationListApiView(ListAPIView):
    serializer_class = NotificationDetailsSerializer
    # pagination_class = OurLimitOffsetPagination
    queryset = NotificationDetails.objects.all()

    def get_queryset(self, *args, **kwargs):
        try:
            return self.queryset.filter(notification_is_deleted=False,
                                        receiver=self.request.user.profile
                                        ).order_by('-notification_created_at')

        except Exception as e:
            logging.error(e)
            return self.queryset.none()

    def get_serializer_context(self):
        context = {"request": self.request}
        return context
