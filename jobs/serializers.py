from rest_framework import serializers
from jobs.models import (
    Jobs,JobBids
)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class JobBidSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)   

    class Meta:
        model = JobBids
        fields = '__all__'
        extra_kwargs = {
            'job': {'required': True},
            'bidder': {'required': False}
        }
        read_only_fields = ('created_at', 'updated_at')
