from rest_framework import viewsets
from django.utils.text import slugify
from .models import BlogPost
from django.shortcuts import render,get_object_or_404
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.paginations import OurLimitOffsetPagination
# Create your views here.

class BlogModelViewSet(viewsets.ModelViewSet):
	# permission_classes = (AllowAny,)
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	pagination_class = OurLimitOffsetPagination

	def get_permissions(self):
		permission_classes = []
		if self.action in ['list', 'retrieve']:
			permission_classes = [AllowAny]
		elif self.action in ['create', 'update', 'partial_update', 'destroy']:
			permission_classes = [IsAuthenticated]
		else:
			permission_classes = [IsAuthenticated]
		return [permission() for permission in permission_classes]

	def perform_create(self, serializer):
		latest_blog = BlogPost.objects.last()
		if latest_blog:
			latest_blog = latest_blog.id + 1
		else:
			latest_blog = 1
		serializer.save(slug=str(latest_blog) + "-" + slugify(serializer.validated_data['title']))
