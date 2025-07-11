import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.environ['SECRET']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
ULTRAMSG_INSTANCE_ID = os.environ['ULTRAMSG_INSTANCE_ID']
ULTRAMSG_TOKEN = os.environ['ULTRAMSG_TOKEN']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedMainfestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR , 'staticfiles')

connection_string = os.environ['AZURE_MYSQL_CONNECTIONSTRING']

parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': parameters['dbname'],  
        'HOST': parameters['host'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
    }
}
