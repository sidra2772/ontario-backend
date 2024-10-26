from rest_framework import serializers
from .models import (
    Report,
    ReportImage,
)
from dashboard.serializers import OrdersSerializer


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = ['id', 'file', 'report']
        read_only_fields = ['id', 'report']


class ReportSerializer(serializers.ModelSerializer):
    report_images = ReportImageSerializer(many=True, read_only=True)
    order = OrdersSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=OrdersSerializer.Meta.model.objects.all(), write_only=True,
                                                  required=False)
    reporter_username = serializers.CharField(source='reporter.user.username', read_only=True)
    receiver_username = serializers.CharField(source='receiver.user.username', read_only=True)
    reporter_image = serializers.ImageField(source='reporter.image', read_only=True)
    receiver_image = serializers.ImageField(source='receiver.image', read_only=True)
    reporter_first_name = serializers.CharField(source='reporter.first_name', read_only=True)
    reporter_last_name = serializers.CharField(source='reporter.last_name', read_only=True)
    reporter_user_type = serializers.CharField(source='reporter.user.user_type', read_only=True)
    receiver_first_name = serializers.CharField(source='receiver.first_name', read_only=True)
    receiver_last_name = serializers.CharField(source='receiver.last_name', read_only=True)
    room = serializers.IntegerField(read_only=True, source='dispute_rooms.room_id')
    client_id = serializers.IntegerField(source='order.client.id', read_only=True)
    client_first_name = serializers.CharField(source='order.client.first_name', read_only=True)
    client_last_name = serializers.CharField(source='order.client.last_name', read_only=True)
    supplier_first_name = serializers.CharField(source='order.service.supplier.first_name', read_only=True)
    supplier_last_name = serializers.CharField(source='order.service.supplier.last_name', read_only=True)
    supplier_id = serializers.IntegerField(source='order.service.supplier.id', read_only=True)

    class Meta:
        model = Report
        fields = [
            'report_number',
            'order',
            'status',
            'subject',
            'order_id',
            'reporter',
            'receiver',
            'client_id',
            'created_at',
            'updated_at',
            'supplier_id',
            'description',
            'reporter_user_type',
            'report_images',
            'reporter_image',
            'receiver_image',
            'client_last_name',
            'client_first_name',
            'receiver_username',
            'reporter_username',
            'reporter_last_name',
            'supplier_last_name',
            'receiver_last_name',
            'receiver_first_name',
            'reporter_first_name',
            'supplier_first_name',
            'room',
            # 'report_ws_room_messages',
        ]


class CreateReportSerializer(serializers.ModelSerializer):
    report_images = ReportImageSerializer(many=True, required=False)

    class Meta:
        model = Report
        fields = [
            'report_number',
            'order',
            'status',
            'subject',
            'reporter',
            'receiver',
            'email',
            'created_at',
            'updated_at',
            'description',
            'report_images',
        ]
        extra_kwargs = {
            'reporter': {'read_only': True},
            'status': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'report_number': {'read_only': True},
        }
