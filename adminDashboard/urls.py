""" This module contains the urls for the adminDashboard app """
from django.urls import path
from django.urls import include
from rest_framework import routers
from adminDashboard.views import (
    BannerViewSet,
    AllUsersAPIView,
    CategoriesViewSet,
    AdminServicesList,
    SocialMediaViewSet,
    AllAdminUserAPIView,
    ReportUpdateAPIView,
    AdminOrdersListView,
    SubCategoriesViewSet,
    ListAdminReportsAPIView,
    RegistrationAdminAPIView,
    UserRetrieveUpdateAPIView,
    SubCategoriesFooterViewSet,
    FooterForCategoriesViewSet,
    AdminOrdersRetrieveAPIView,
    AdminServicesRetrieveUpdate,
    HeaderForCategoriesPageViewSet,
    FrequentlyAskedQuestionViewSet,
    AdminUpdatePaymentStatusAPIView,
    SubCategoriesQuestionAndAnswerViewSet,
    SubCategoriesFrequentlyAskedQuestionViewSet,
    DashboardView,
    MonthlySalesView,
    AdminUpdateStatusAPIView

)

router = routers.DefaultRouter()
router.register('banner', BannerViewSet)
router.register('categories', CategoriesViewSet)
router.register('social-media', SocialMediaViewSet)
router.register('sub-categories', SubCategoriesViewSet)
router.register('sub-categories-footer', SubCategoriesFooterViewSet)
router.register('footer-for-categories', FooterForCategoriesViewSet)
router.register('header-for-categories', HeaderForCategoriesPageViewSet)
router.register('home-page-frequently-asked-questions',
                FrequentlyAskedQuestionViewSet)
router.register('sub-categories-question-and-answer',
                SubCategoriesQuestionAndAnswerViewSet)
router.register('sub-categories-frequently-asked-question',
                SubCategoriesFrequentlyAskedQuestionViewSet)

urlpatterns = [
    path('orders/', AdminOrdersListView.as_view(), name='orders'),
    path('services/', AdminServicesList.as_view(), name='services'),
    path('all-users/', AllUsersAPIView.as_view(), name='all-users'),
    path('all-admin-user/', AllAdminUserAPIView.as_view(), name='all-admin-user'),
    path('register-admin/', RegistrationAdminAPIView.as_view(), name='register-admin'),
    path('report-update/<str:report_number>/', ReportUpdateAPIView.as_view(), name='report-update'),
    path('services/<int:pk>/', AdminServicesRetrieveUpdate.as_view(), name='services-update'),
    path('list-admin-reports/', ListAdminReportsAPIView.as_view(), name='list-admin-reports'),
    path('retrieve-orders/<str:order_number>/', AdminOrdersRetrieveAPIView.as_view(), name='orders-retrieve'),
    path('user-retrieve-update/<str:username>/', UserRetrieveUpdateAPIView.as_view(), name='admin-retrieve-update'),
    path('update-payment-status/<str:order_number>/', AdminUpdatePaymentStatusAPIView.as_view(),
         name='update-payment-status'),
    path('month-sales/', MonthlySalesView.as_view(), name='month-sales'),
    path('dashboard-analytics/', DashboardView.as_view(), name='dashboard'),
    path('order-update-status/<str:order_number>/', AdminUpdateStatusAPIView.as_view(), name='update-status'),
    path('', include(router.urls)),
]
