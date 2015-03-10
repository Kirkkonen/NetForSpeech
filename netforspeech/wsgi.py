"""
WSGI config for netforspeech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if "DJANGO_SETTINGS_MODULE" in os.environ.keys():
    application = get_wsgi_application()
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netforspeech.settings.prod_settings")
    from dj_static import Cling
    application = Cling(get_wsgi_application())
