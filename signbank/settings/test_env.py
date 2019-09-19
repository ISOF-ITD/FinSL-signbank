# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from signbank.settings.production import *
# settings.base imports settings_secret
# The following settings are defined in settings_secret:
# SECRET_KEY, ADMINS, DATABASES, EMAIL_HOST, EMAIL_PORT, DEFAULT_FROM_EMAIL

# IMPORTANT: Debug should always be False in production
DEBUG = True

# This points to the wsgi.py file that is used in tools.py to make web server "reload" the application.
# WSGI_FILE = '/home/signbank/signbank-fi/signbank/wsgi.py'
WSGI_FILE = '/var/www/django/teckenlistan/signbank/wsgi_test_env.py'
