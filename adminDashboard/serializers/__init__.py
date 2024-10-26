""" This package contains all the serializers for the admin dashboard. """
from .assets import AdminCategoriesSerializer, AdminSubCategoriesSerializer
from .user import CreateAdminUserSerializer, AllAdminUserSerializer, AllUsersSerializer
from .services import AdminServicesSerializer
from .reports import AdminReportSerializer
from .orders import AdminOrdersSerializer, AdminUpdatePaymentStatusSerializer, AdminUpdateStatusSerializer
from .publicpagescontent import (
    HeaderForCategoriesPageSerializer,
    FooterForCategoriesSerializer,
    SubCategoriesFrequentlyAskedQuestionSerializer,
    SubCategoriesQuestionAndAnswerSerializer,
    SubCategoriesFooterSerializer,
)
