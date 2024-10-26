from django.urls import path
from django.urls import include
from rest_framework import routers
from dashboard.views import (
    OrdersViewSet,
    FeedbackViewSet,
    SupplierFeedbackViewSet,
    CancelOrderStatusAPIView,
    UpdatePaymentStatusAPIView,
    ClientDashboardView,
    ClientMonthSpendingView,
    ClientMonthlyNumberOfOrdersView,
    SupplierDashboardView,
    SupplierMonthIncomeView, SupplierMonthlyNumberOfOrdersView,
)

router = routers.DefaultRouter()
router.register('orders', OrdersViewSet)
router.register('feedbacks', FeedbackViewSet)
router.register('supplier-feedbacks', SupplierFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update-payment-status/<str:order_number>/', UpdatePaymentStatusAPIView.as_view()),
    path('cancel-order-status/<str:order_number>/', CancelOrderStatusAPIView.as_view()),
    path('client-month-spending/', ClientMonthSpendingView.as_view(), name='month-sales'),
    path('client-monthly-number-of-orders/', ClientMonthlyNumberOfOrdersView.as_view(), name='monthly-orders'),
    path('client-dashboard-analytics/', ClientDashboardView.as_view(), name='dashboard'),
    path('supplier-dashboard-analytics/', SupplierDashboardView.as_view(), name='supplier-dashboard'),
    path('supplier-monthly-income/', SupplierMonthIncomeView.as_view(), name='supplier-month-sales'),
    path('supplier-monthly-number-of-orders/', SupplierMonthlyNumberOfOrdersView.as_view(),
         name='supplier-monthly-orders')
]
