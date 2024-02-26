"""
ASGI config.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_calendar_clone.settings")

application = get_asgi_application()
