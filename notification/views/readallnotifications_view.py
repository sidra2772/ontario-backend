""" This module is used to mark all notifications as read."""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notification.models import NotificationDetails


class ReadAllNotificationAPIView(APIView):
    """ This api is used to mark all notifications as read """

    def post(self, request):
        """ This api is used to mark all notifications as read"""
        NotificationDetails.objects.filter(receiver=request.user.profile,
                                           notification_is_read=False).update(
            notification_is_read=True)
        return Response({"message": "Notification updated successfully"}, status=status.HTTP_200_OK)
