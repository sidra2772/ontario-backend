from rest_framework import serializers
from helpandsupport.models import Report, ReportImage


class AdminReportImage(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = '__all__'


class AdminReportSerializer(serializers.ModelSerializer):
    report_images = AdminReportImage(many=True, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'
