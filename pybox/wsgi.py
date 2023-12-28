"""
WSGI config for pybox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

django_env = os.environ.get("DJANGO_ENV", "local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"pybox.settings.{django_env}")

application = get_wsgi_application()
