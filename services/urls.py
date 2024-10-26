from django.urls import path
from django.urls import include
from rest_framework import routers
from services.views import ServicesViewSet, PopularServicesViewSet
from services.views import ApplicationViewSet

router = routers.DefaultRouter()
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
    path('popular-services/', PopularServicesViewSet.as_view(), name='popular-services'),
]
