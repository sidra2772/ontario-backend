"""coresite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Supportify API's",
        default_version='v1',
        description="Supportify API's for user, chat, assets, profile, notification, admin-dashboard, etc.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shamsulhaq@beyonderissolutions.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('core.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/assets/', include('assets.urls')),
    path('api/service/', include('services.urls')),
    path('api/home-page/', include('homePage.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/profile/', include('userprofile.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/notification/', include('notification.urls')),
    path('api/categories/', include('categoriespage.urls')),
    path('api/help-support/', include('helpandsupport.urls')),
    path('api/admin-dashboard/', include('adminDashboard.urls')),
    path('api/sub-categories/', include('subcategoriespage.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
