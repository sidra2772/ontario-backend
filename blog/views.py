from rest_framework import viewsets
from django.utils.text import slugify
from .models import BlogPost, Events, EventBookings
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import BlogPostSerializer, EventsSerializer, EventBookingsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.paginations import OurLimitOffsetPagination
# Create your views here.


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
