"""This module contains the NotificationDetails model for the notification app."""
from django.db import models


class NotificationDetails(models.Model):
    """This class contains the NotificationDetails model for the notification app."""
    sender = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name="sender_notification")
    receiver = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE,
                                 related_name="receiver_notification")
    heading = models.CharField(max_length=100, blank=True, null=True)
    message = models.ForeignKey(
        "chat.RoomMessage", on_delete=models.CASCADE, related_name="message_notification", null=True, blank=True)
    plain_text = models.CharField(max_length=100, blank=True, null=True)
    service = models.ForeignKey(
        "services.Services", on_delete=models.CASCADE, related_name="service_notification", null=True, blank=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    order = models.ForeignKey(
        "dashboard.Orders", on_delete=models.CASCADE, related_name="order_notification", null=True, blank=True)
    notification_type = models.CharField(max_length=255)
    report = models.ForeignKey(
        'helpandsupport.Report', on_delete=models.CASCADE, related_name='report_notification', null=True, blank=True)
    notification_created_at = models.DateTimeField(auto_now_add=True)
    notification_updated_at = models.DateTimeField(auto_now=True)
    notification_is_read = models.BooleanField(default=False)
    notification_is_deleted = models.BooleanField(default=False)
    notification_is_archived = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.plain_text)
