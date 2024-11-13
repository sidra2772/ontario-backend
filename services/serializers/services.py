from rest_framework import serializers
from services.models import Services
from dashboard.serializers import SupplierFeedbackSerializer


class ServicesSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize the services. """
    category = serializers.IntegerField(source='sub_category.category.id', read_only=True)
    category_name = serializers.CharField(source='sub_category.category.name', read_only=True)
    category_slug = serializers.CharField(source='sub_category.category.category_slug', read_only=True)
    sub_category_slug = serializers.CharField(source='sub_category.subcategory_slug', read_only=True)
    sub_category_name = serializers.CharField(source='sub_category.name', read_only=True)
    currency = serializers.CharField(source='currency.name', read_only=True)
    currency_code = serializers.CharField(source='currency.code', read_only=True)
    supplier_username = serializers.CharField(source='supplier.user.username', read_only=True)
    supplier_first_name = serializers.CharField(source='supplier.first_name', read_only=True)
    supplier_last_name = serializers.CharField(source='supplier.last_name', read_only=True)
    supplier_image = serializers.ImageField(source='supplier.image', read_only=True)
    service_feedback = SupplierFeedbackSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Services
        exclude = ['is_active', ]
        read_only_fields = ['supplier', 'service_slug', 'created_at', 'updated_at']
