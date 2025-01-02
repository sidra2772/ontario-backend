from .views import BlogModelViewSet, ListEvents, CreateBooking, RetrieveEvent
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'blogs', BlogModelViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('events/', ListEvents.as_view(), name='list-events'),
    path('create-booking/', CreateBooking.as_view(), name='create-booking'),
    path('event/<int:pk>/', RetrieveEvent.as_view(), name='retrieve-event'),
]