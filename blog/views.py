from rest_framework import viewsets
from django.utils.text import slugify

from coresite.mixin.permission_mixin import IsAdminUser
from .models import BlogPost, Events, EventBookings, NewsAndUpdates
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import BlogPostSerializer, EventsSerializer, EventBookingsSerializer, NewsAndUpdatesSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.paginations import OurLimitOffsetPagination
from django_filters import rest_framework as backend_filters
from rest_framework import filters
# Create your views here.


class CreateNewsAndUpdates(CreateAPIView):
	serializer_class = NewsAndUpdatesSerializer
	queryset = NewsAndUpdates.objects.all()
	permission_classes = [IsAdminUser]

class ListNewsAndUpdates(ListAPIView):
	serializer_class = NewsAndUpdatesSerializer
	queryset = NewsAndUpdates.objects.all()
	permission_classes = [AllowAny]
	pagination_class = OurLimitOffsetPagination

class RetrieveNewsAndUpdates(RetrieveAPIView):
	serializer_class = NewsAndUpdatesSerializer
	queryset = NewsAndUpdates.objects.all()
	permission_classes = [AllowAny]

class CreateBooking(CreateAPIView):
	serializer_class = EventBookingsSerializer
	queryset = EventBookings.objects.all()
	permission_classes = [AllowAny]

class ListEvents(ListAPIView):
	serializer_class = EventsSerializer
	queryset = Events.objects.all()
	permission_classes = [AllowAny]
	pagination_class = OurLimitOffsetPagination

class RetrieveEvent(RetrieveAPIView):
	serializer_class = EventsSerializer
	queryset = Events.objects.all()
	permission_classes = [AllowAny]



class BlogModelViewSet(viewsets.ModelViewSet):
	# permission_classes = (AllowAny,)
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	pagination_class = OurLimitOffsetPagination
	filter_backends = [
		backend_filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
	]
	search_fields = ['title', 'content']
	ordering_fields = ['created_at']
	filterset_fields = ['author','blog_category']

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
		serializer.save(author=self.request.user.profile)
