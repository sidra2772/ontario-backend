from rest_framework import serializers
from jobs.models import (
    Jobs,JobBids
)


class JobSerializer(serializers.ModelSerializer):
    is_bid = serializers.BooleanField(read_only=True)
    class Meta:
        model = Jobs
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class JobBidSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)   
    job_user_first_name = serializers.CharField(source='job.user.first_name', read_only=True)
    job_user_last_name = serializers.CharField(source='job.user.last_name', read_only=True)
    job_user_username= serializers.CharField(source='job.user.username', read_only=True)


    class Meta:
        model = JobBids
        fields = '__all__'
        extra_kwargs = {
            'job': {'required': True},
            'bidder': {'required': False}
        }
        read_only_fields = ('created_at', 'updated_at')
