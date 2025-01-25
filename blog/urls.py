from .views import BlogModelViewSet, ListEvents, CreateBooking, RetrieveEvent, CreateNewsAndUpdates, ListNewsAndUpdates, RetrieveNewsAndUpdates
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'blogs', BlogModelViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('events/', ListEvents.as_view(), name='list-events'),
    path('create-booking/', CreateBooking.as_view(), name='create-booking'),
    path('event/<int:pk>/', RetrieveEvent.as_view(), name='retrieve-event'),
    path('create-news-and-updates/', CreateNewsAndUpdates.as_view(), name='create-news-and-updates'),
    path('news-and-updates/', ListNewsAndUpdates.as_view(), name='list-news-and-updates'),
    path('news-and-updates/<int:pk>/', RetrieveNewsAndUpdates.as_view(), name='retrieve-news-and-updates'),

]