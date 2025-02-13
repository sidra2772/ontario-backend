import os
import sys

# Path to the virtual environment's Python interpreter
INTERP = "/home/onmaxmls/virtualenv/ontario-backend/3.12/bin/python"

# Ensure the script is running with the correct Python interpreter
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Ensure the project directory is in sys.path
sys.path.insert(0, "/home/onmaxmls/ontario-backend")

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coresite.settings")

# Import and set up the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
