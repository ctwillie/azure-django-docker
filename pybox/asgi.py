"""
ASGI config for pybox project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

django_env = os.environ.get("DJANGO_ENV", "local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"pybox.settings.{django_env}")

application = get_asgi_application()
