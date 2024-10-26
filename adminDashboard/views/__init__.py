from .assets import CategoriesViewSet, SubCategoriesViewSet
from .user import RegistrationAdminAPIView, AllAdminUserAPIView, AllUsersAPIView, UserRetrieveUpdateAPIView
from .reports import ReportUpdateAPIView, ListAdminReportsAPIView
from .orders import (
    AdminOrdersListView,
    AdminOrdersRetrieveAPIView,
    AdminUpdateStatusAPIView,
    AdminUpdatePaymentStatusAPIView,
)
from .services import AdminServicesList, AdminServicesRetrieveUpdate
from .publicpagescontent import (
    FooterForCategoriesViewSet,
    HeaderForCategoriesPageViewSet,
    SubCategoriesFrequentlyAskedQuestionViewSet,
    SubCategoriesQuestionAndAnswerViewSet, SubCategoriesFooterViewSet,
)
from .homePage import (
    BannerViewSet,
    FrequentlyAskedQuestionViewSet,
    SocialMediaViewSet,
)
from .dashboard import DashboardView, MonthlySalesView
