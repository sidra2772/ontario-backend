from .models  import BlogPost, Events, EventBookings
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name', read_only=True)
    # category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = BlogPost
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'



class EventBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBookings
        fields = '__all__'


