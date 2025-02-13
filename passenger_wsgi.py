# import os
# import sys
#
# # Path to the Python interpreter in your virtual environment.
# VENV_PYTHON = "/home/onmaxmls/virtualenv/ontario-backend/3.12/bin/python"
#
# # Re-execute with the correct Python interpreter if needed.
# if sys.executable != VENV_PYTHON:
#     os.execl(VENV_PYTHON, VENV_PYTHON, *sys.argv)
#
# # Ensure current directory is in sys.path
# sys.path.append(os.getcwd())
#
# # Set the Django settings module
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coresite.settings")
#
# # Import ASGI and Channels components.
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing as channels_routing
# import notification.routing as notification_routing
# from chat.middlewares import TokenAuthMiddleware
#
# # Initialize Django ASGI application for handling traditional HTTP requests.
# django_asgi_app = get_asgi_application()
#
# # Define the overall ASGI application routing.
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": TokenAuthMiddleware(
#         URLRouter(
#             channels_routing.websocket_urlpatterns +
#             notification_routing.websocket_urlpatterns
#         )
#     ),
# })
#
from django.core.wsgi import get_wsgi_application
import sys
import os
INTERP = "/home/onmaxmls/virtualenv/ontario-backend/3.12/bin/python"
# INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "coresite.settings"
application = get_wsgi_application()
