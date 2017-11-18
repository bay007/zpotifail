## este sera de desarrollo local

from .base import *
import os

SECRET_KEY = '%a-8=sdv0^++)=)05i9!5-u$!ve8lfwh89q#l=jja9u+7+8ppu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'egpahrez',
        'USER': 'egpahrez',
        'PASSWORD': 'N3C0FlJ_RFkirYDh3rncxwlbaIPvNvTF',
        'HOST': 'baasu.db.elephantsql.com',
        'PORT': '5432'
    }
}

# busca estaticos en local
STATICFILES_DIRS=[os.path.join(os.getcwd(),"static")]