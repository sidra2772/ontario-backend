"""
ASGI config for coresite project.
"""

import os
import django

# Set the Django settings module explicitly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coresite.settings')

# Initialize Django
django.setup()

# Now import ASGI-related modules
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.middlewares import TokenAuthMiddleware
import chat.routing as chat_routing
import notification.routing as notification_routing

# Define ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            chat_routing.websocket_urlpatterns + notification_routing.websocket_urlpatterns
        )
    ),
})
