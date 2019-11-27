# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from signbank.settings.production import *

# settings.base imports settings_secret
# The following settings are defined in settings_secret:
# SECRET_KEY, ADMINS, DATABASES, EMAIL_HOST, EMAIL_PORT, DEFAULT_FROM_EMAIL

ENVIRONMENT_URL = 'https://frigg.sprakochfolkminnen.se/' + PROJECT_NAME
