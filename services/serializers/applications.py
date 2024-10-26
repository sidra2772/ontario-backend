from rest_framework import serializers
from services.models import Applications


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'