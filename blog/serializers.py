from .models  import BlogPost, Events, EventBookings
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name', read_only=True)
    author_username = serializers.CharField(source='author.user.username', read_only=True)
    author_email = serializers.CharField(source='author.user.email', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    author_bio = serializers.CharField(source='author.bio', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author = serializers.IntegerField(source='author.id', read_only=True)

    
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


