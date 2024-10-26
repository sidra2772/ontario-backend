from rest_framework import serializers
from categoriespage.models import HeaderforCategoriesPage

class HeaderforCategoriesPageSerializer(serializers.ModelSerializer):
    """
    Header For Categories Page Serializer
    """
    class Meta:
        model = HeaderforCategoriesPage
        fields = '__all__'