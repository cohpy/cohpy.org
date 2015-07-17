from .base import *


DEBUG = True
SECRET_KEY = 'Some kinda secret'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cohpy',
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
)

