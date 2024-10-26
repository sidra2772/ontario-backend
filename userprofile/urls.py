from django.urls import path, include
from django.urls import re_path
from .views import UserProfileViewSet, RetrieveAndUpdateUserProfile, CompanyEmployeeList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-profile', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
    path('update/<str:username>/', RetrieveAndUpdateUserProfile.as_view(), name='update-user-profile'),
    path('company-employee/', CompanyEmployeeList.as_view(), name='company-employee-list'),

]
