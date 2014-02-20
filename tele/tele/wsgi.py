"""
WSGI config for tele project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os,site
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tele.settings")

site.addsitedir('/home/mateo/Python/boiler-room/tele')
site.addsitedir('/home/mateo/.virtualenvs/boiler-room/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
