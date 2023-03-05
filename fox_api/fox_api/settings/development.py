from .base import *  # noqa
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
