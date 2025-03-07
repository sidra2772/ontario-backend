CORS_ORIGIN_ALLOW_ALL = False  # Change to False for security
CORS_ALLOW_CREDENTIALS = True  # WebSockets often require credentials

CORS_ALLOWED_ORIGINS = [
    "https://portal.onma.ca",
    "https://backend.onma.ca",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "dnt",
    "accept",
    "origin",
    "user-agent",
    "x-csrftoken",
    "content-type",
    "authorization",
    "accept-encoding",
    "x-requested-with",
    "access-control-allow-origin",
]

# Allow WebSocket requests
CORS_ALLOW_ALL_ORIGINS = True  # Temporary for debugging

ALLOWED_HOSTS = [
    "portal.onma.ca",
    "backend.onma.ca",
    "your-api.com",
    "18.224.30.203",
    "localhost",
    "127.0.0.1",
    "*",  # Allow everything (for debugging)
]

# WebSockets settings (for Django Channels)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
