SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header',
#         }
#     },
#     'USE_SESSION_AUTH': False,  # Disable Django session auth for Swagger
# }

# Swagger settings for drf-yasg
# SWAGGER_SETTINGS = {
#     # 'USE_SESSION_AUTH': False,
#     # 'SECURITY_DEFINITIONS': {
#     #     'Basic': {
#     #         'type': 'basic'
#     #     },
#     # },
#     'DEFAULT_API_URL': 'https://staging.thesupportify.com/'
# }

# Swagger settings for drf-spectacular
# SPECTACULAR_SETTINGS = {
#     'SERVERS': [
#         {'url': 'https://staging.thesupportify.com/', 'description': 'Production server'}
#     ],
# }
