from .models  import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name', read_only=True)
    # category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = BlogPost
        fields = '__all__'

