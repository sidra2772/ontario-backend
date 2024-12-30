from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobBidViewSet, JobViewSet


router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('job-bids', JobBidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]