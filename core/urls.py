from django.urls import path
from core.views import (
    UserDetailView,
    RegistrationView,
    EmailExistAPIView,
    ForgetPasswordView,
    ChangePasswordView,
    ResetPasswordAPIView,
    AccountStatusAPIView,
    AccountActivationAPIView,
    ResendActivationAPIView,
    RegisterBusinessMemberView,
    CustomTokenObtainPairView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('register/business-member/', RegisterBusinessMemberView.as_view(), name='register-business-member'),
    path('account/activation/<secret_key>', AccountActivationAPIView.as_view(),
         name='account-activation'),
    path('resend/activation/', ResendActivationAPIView.as_view(), name='resend-activation'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', UserDetailView.as_view(), name='user'),
    path('forget/password/', ForgetPasswordView.as_view(), name='forget_password'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('reset/password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('email-exist/', EmailExistAPIView.as_view(), name='email-exist'),
    path('account-status/', AccountStatusAPIView.as_view(), name='account-status'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # path('google/login/', GoogleLoginView.as_view(), name='google-login'),

]
