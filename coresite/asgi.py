"""
ASGI config for coresite project.
"""

import os
import django
from django.core.asgi import get_asgi_application

# Initialize Django FIRST
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coresite.settings')
django.setup()

# Now import other dependencies AFTER initialization
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.middlewares import TokenAuthMiddleware
import chat.routing as channels_routing
import notification.routing as notification_routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            channels_routing.websocket_urlpatterns +
            notification_routing.websocket_urlpatterns
        )
    )
})