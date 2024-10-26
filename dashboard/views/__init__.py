from .orders import OrdersViewSet, UpdatePaymentStatusAPIView, CancelOrderStatusAPIView
from .feedbacks import FeedbackViewSet, SupplierFeedbackViewSet
from .dashboard import (
    ClientDashboardView, ClientMonthSpendingView, SupplierDashboardView,
    ClientMonthlyNumberOfOrdersView,
    SupplierMonthIncomeView, SupplierMonthlyNumberOfOrdersView,
)
