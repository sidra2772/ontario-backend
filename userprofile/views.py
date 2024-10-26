from rest_framework import viewsets
from .models import UserProfile
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from utils.paginations.pagination import LimitOffsetPagination
from django_filters import rest_framework as backend_filters
from .filters import UserProfileFilter
from .serializers import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_class = UserProfileFilter
    search_fields = ['first_name', 'last_name', 'user__username']
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.queryset.filter(user__is_active=True)
        return self.queryset.filter(user__is_active=True, user=self.request.user)


class CompanyEmployeeList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_class = UserProfileFilter
    search_fields = ['first_name', 'last_name', 'user__username']

    def get_queryset(self):
        if self.request.user.profile.account_type == 'business_admin':
            return self.queryset.filter(business_profile=self.request.user.profile.business_profile)
        return self.queryset.none()


class RetrieveAndUpdateUserProfile(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        if self.request.user.profile.account_type == 'business_admin':
            return self.queryset.filter(business_profile=self.request.user.profile.business_profile)
        return self.queryset.none()
