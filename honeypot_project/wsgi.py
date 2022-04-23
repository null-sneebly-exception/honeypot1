"""
WSGI config for honeypot_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/ubuntu")
sys.path.append("/home/ubuntu/honeypot_project")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'honeypot_project.settings')

application = get_wsgi_application()
