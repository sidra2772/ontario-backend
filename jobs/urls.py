from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobBidViewSet, JobViewSet


router = DefaultRouter()
router.register('jobs', JobViewSet,basename='jobs')
router.register('job-bids', JobBidViewSet,basename='job-bids')

urlpatterns = [
    path('', include(router.urls)),
]