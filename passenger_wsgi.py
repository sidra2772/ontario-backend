from django.core.asgi import get_asgi_application
import sys
import os
INTERP = "/home/onmaxmls/virtualenv/ontario-backend/3.12/bin/activate"
# INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "coresite.settings"
import chat.routing as channels_routing
import notification.routing as notification_routing
from chat.middlewares import TokenAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            channels_routing.websocket_urlpatterns+notification_routing.websocket_urlpatterns


        ),

    )
}
)
