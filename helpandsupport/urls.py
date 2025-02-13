from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ReportViewSet, ReportImageDeleteAPIView, NewsLetterAPIView

router = routers.DefaultRouter()
router.register('report', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('report-image-delete/<int:pk>/', ReportImageDeleteAPIView.as_view()),
    path('newsletter/', NewsLetterAPIView.as_view())
]
