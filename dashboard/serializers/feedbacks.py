from dashboard.models import ClientFeedback, SupplierFeedback
from rest_framework import serializers


class ClientFeedbackSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the data of Feedback model. """
    client_first_name = serializers.CharField(source='order.client.first_name', read_only=True)
    client_last_name = serializers.CharField(source='order.client.last_name', read_only=True)
    client_email = serializers.CharField(source='order.client.user.email', read_only=True)
    client_username = serializers.CharField(source='order.client.user.username', read_only=True)
    client_image = serializers.ImageField(source='order.client.image', read_only=True)
    supplier_username = serializers.CharField(source='order.service.supplier.user.username', read_only=True)
    supplier_email = serializers.CharField(source='order.service.supplier.user.email', read_only=True)
    supplier_image = serializers.ImageField(source='order.service.supplier.image', read_only=True)
    supplier_first_name = serializers.CharField(source='order.service.supplier.first_name', read_only=True)
    supplier_last_name = serializers.CharField(source='order.service.supplier.last_name', read_only=True)

    class Meta:
        """ Metaclass for serializer """
        model = ClientFeedback
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', ]


class SupplierFeedbackSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the data of Feedback model. """
    supplier_username = serializers.CharField(source='service.supplier.user.username', read_only=True)
    supplier_email = serializers.CharField(source='service.supplier.user.email', read_only=True)
    supplier_image = serializers.ImageField(source='service.supplier.image', read_only=True)
    supplier_first_name = serializers.CharField(source='service.supplier.first_name', read_only=True)
    supplier_last_name = serializers.CharField(source='service.supplier.last_name', read_only=True)
    client_first_name = serializers.CharField(source='order.client.first_name', read_only=True)
    client_last_name = serializers.CharField(source='order.client.last_name', read_only=True)
    client_email = serializers.CharField(source='order.client.user.email', read_only=True)
    client_username = serializers.CharField(source='order.client.user.username', read_only=True)
    client_image = serializers.ImageField(source='order.client.image', read_only=True)

    class Meta:
        """ Metaclass for serializer """
        model = SupplierFeedback
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', ]
