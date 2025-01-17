from dashboard.models import Orders
from rest_framework import serializers
from .feedbacks import ClientFeedbackSerializer, SupplierFeedbackSerializer


class OrdersSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the orders. """
    client_first_name = serializers.CharField(source='client.first_name', read_only=True)
    client_last_name = serializers.CharField(source='client.last_name', read_only=True)
    client_email = serializers.CharField(source='client.user.email', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    service_image = serializers.ImageField(source='service.image', read_only=True)
    client_username = serializers.CharField(source='client.user.username', read_only=True)
    client_image = serializers.ImageField(source='client.image', read_only=True)
    supplier_username = serializers.SerializerMethodField()
    supplier_email = serializers.SerializerMethodField()
    supplier_image = serializers.SerializerMethodField()
    supplier_first_name = serializers.SerializerMethodField()
    supplier_last_name = serializers.SerializerMethodField()
    supplier_id = serializers.SerializerMethodField()
    job_title = serializers.CharField(source='job.job.title', read_only=True)

    order_feedback = ClientFeedbackSerializer(read_only=True)
    order_feedback_supplier = SupplierFeedbackSerializer(read_only=True)

    def get_supplier_username(self, obj):
        if obj.service:
            return obj.service.supplier.user.username
        if obj.job:
            return obj.job.bidder.user.username
        return None

    def get_supplier_email(self, obj):
        if obj.service:
            return obj.service.supplier.user.email
        if obj.job:
            return obj.job.bidder.user.email
        return None

    def get_supplier_image(self, obj):
        # if obj.service:
        #     return obj.service.supplier.image
        # if obj.job:
        #     return obj.job.bidder.image
        return None

    def get_supplier_first_name(self, obj):
        if obj.service:
            return obj.service.supplier.first_name
        if obj.job:
            return obj.job.bidder.first_name
        return None

    def get_supplier_last_name(self, obj):
        if obj.service:
            return obj.service.supplier.last_name
        if obj.job:
            return obj.job.bidder.last_name
        return None

    def get_supplier_id(self, obj):
        if obj.service:
            return obj.service.supplier.id
        if obj.job:
            return obj.job.bidder.id
        return None

    class Meta:
        model = Orders
        fields = '__all__'
        read_only_fields = ['order_number', 'hiring_date', 'created_at', 'updated_at', 'payment_status']


class SupplierUpdatePaymentSerializer(serializers.ModelSerializer):
    """ This serializer is used to update the payment status of the supplier. """

    class Meta:
        model = Orders
        fields = ['payment_status']
        read_only_fields = ['order_number', 'client', 'hiring_date', 'created_at', 'updated_at']


class CancelOrderSerializer(serializers.ModelSerializer):
    """ This serializer is used to cancel the order. """

    class Meta:
        model = Orders
        fields = ['status', 'cancel_reason']
        read_only_fields = ['order_number', 'client', 'hiring_date', 'created_at', 'updated_at']
