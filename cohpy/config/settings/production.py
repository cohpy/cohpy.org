from .base import *

# TODO in production environment need to create .env file containing
# SECRET_KEY, can put explicit path into the following
# https://github.com/joke2k/django-environ

environ.Env.read_env() # reading .env file

SECRET_KEY = env('SECRET_KEY')