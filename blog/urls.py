from django.contrib import admin
from .views import BlogModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'blogs', BlogModelViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]