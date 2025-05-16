import os

from .base import *


DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cohpy',
    }
}

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


INSTALLED_APPS += (
    'debug_toolbar',
)

