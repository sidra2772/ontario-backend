from .environment import env, os, BASE_DIR
from .application import (
    DJANGO_APPLICATIONS,
    CUSTOM_APPLICATIONS,
    THIRD_PARTY_APPLICATIONS,
)

SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

DOMAIN = env("DOMAIN")
ROOT_URLCONF = 'coresite.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.contenttypes',

    # Third-party apps (Daphne must be before django.contrib.staticfiles)
    'daphne',  # Move this before 'django.contrib.staticfiles'

    'admin_interface',
    'storages',
    'colorfield',
    'django_ckeditor_5',
    'drf_yasg',
    'channels',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',

    # Django static files app
    'django.contrib.staticfiles',

    # Custom apps
    'core',
    'jobs',
    'chat',
    'blog',
    'assets',
    'services',
    'homePage',
    'dashboard',
    'userprofile',
    'notification',
    'helpandsupport',
    'adminDashboard',
    'subcategoriespage',
    'categoriespage',
]


ASGI_APPLICATION = 'coresite.asgi.application'
WSGI_APPLICATION = 'coresite.wsgi.application'

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL.replace("redis://", "rediss://")],  # Force TLS if needed
        },
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
DJANGO_SETTINGS_MODULE='coresite.settings'

USE_TZ = True
COMPANY_NAME = env("COMPANY_NAME")
COMPANY_COPYRIGHT = env("COMPANY_COPYRIGHT")
COMPANY_EMAIL = env("COMPANY_EMAIL")
COMPANY_PHONE = env("COMPANY_PHONE")
COMPANY_WEBSITE = env("COMPANY_WEBSITE")
COMPANY_LOGO = env("COMPANY_LOGO")
COMPANY_LOGO_TEXT = env("COMPANY_LOGO_TEXT")
PRIMARY_COLOR = env("PRIMARY_COLOR")
SECONDARY_COLOR = env("SECONDARY_COLOR")
BUTTON_COLOR = env("BUTTON_COLOR")
TEXT_COLOR = env("TEXT_COLOR")
STARTING_YEAR = env("COMPANY_STARTING_YEAR")
FAVICON = env("FAVICON")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REACT_DOMAIN = env("REACT_DOMAIN")

NON_BUSINESS_EMAILS = env("NON_BUSINESS_EMAILS", cast=lambda v: [
    s.strip() for s in v.split(',')])