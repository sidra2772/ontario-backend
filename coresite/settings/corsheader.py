CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_METHODS = (
    'GET',
    'PUT',
    'POST',
    'PATCH',
    'DELETE',
    'OPTIONS',
)

CORS_ALLOW_HEADERS = (
    'dnt',
    'accept',
    'origin',
    'user-agent',
    'x-csrftoken',
    'Content-Type',
    'content-type',
    'authorization',
    'accept-encoding',
    'x-requested-with',
    'access-control-allow-origin',
    'Access-Control-Allow-Origin',
)


CORS_ALLOWED_ORIGINS = [
    "https://portal.onma.ca",
    "http://localhost:3000",
    "https://backend.onma.ca",  # If testing locally
]

CSRF_TRUSTED_ORIGINS = [
    "https://portal.onma.ca",
    "http://localhost:3000",
    "https://backend.onma.ca"
]

ALLOWED_HOSTS = ["portal.onma.ca", "your-api.com", "18.224.30.203", "localhost","18.224.30.203","backend.onma.ca","127.0.0.1","localhost"]
