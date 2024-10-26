from rest_framework import serializers
from notification.models import NotificationImage
from notification.models import NotificationDetails
import logging
from dashboard.serializers import OrdersSerializer


class NotificationDetailsSerializer(serializers.ModelSerializer):
    """
    serializer for notification details
    """

    notification_image = serializers.SerializerMethodField()
    sender_image = serializers.ImageField(
        source='sender.image', read_only=True)
    sender_name = serializers.CharField(
        source='sender.user.username', read_only=True)
    sender_last_name = serializers.CharField(
        source='sender.last_name', read_only=True)
    sender_first_name = serializers.CharField(
        source='sender.first_name', read_only=True)
    sender_user_type = serializers.CharField(
        source='sender.user.user_type', read_only=True)
    is_user_online = serializers.BooleanField(
        source='sender.is_online', read_only=True)
    receiver_user_type = serializers.CharField(
        source='receiver.user.user_type', read_only=True)
    unread_notification_count = serializers.SerializerMethodField()
    service_name = serializers.CharField(
        source='service.name', read_only=True)
    order = OrdersSerializer()
    room_id = serializers.IntegerField(
        source='message.room.id', read_only=True)
    service_slug = serializers.CharField(
        source='service.service_slug', read_only=True)
    report_number = serializers.CharField(
        source='report.report_number', read_only=True)

    class Meta:
        model = NotificationDetails
        fields = [
            'id',
            'order',
            'sender',
            'heading',
            'message',
            'room_id',
            'receiver',
            'service',
            'service_name',
            'plain_text',
            'report_number',
            'sender_name',
            'description',
            'service_slug',
            'sender_user_type',
            'receiver_user_type',
            'sender_image',
            'is_user_online',
            'sender_last_name',
            'sender_first_name',
            'notification_type',
            'notification_image',
            'notification_is_read',
            'notification_created_at',
            'notification_is_deleted',
            'unread_notification_count',
        ]

    def get_notification_image(self, obj):
        try:
            image = NotificationImage.objects.all()
            if image:
                return image[-1].image.url
            else:
                return None
        except Exception as e:
            logging.error(e)
            return None

    def get_unread_notification_count(self, obj):
        return NotificationDetails.objects.filter(notification_is_read=False, receiver=obj.receiver).count()
