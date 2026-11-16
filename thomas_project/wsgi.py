"""
WSGI config for thomas_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# manage.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thomas_project.settings.development')

#wsgi.py (production server read this)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thomas_project.settings.production')

application = get_wsgi_application()
