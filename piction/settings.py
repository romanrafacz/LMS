"""
Django settings for piction project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+#!%q0+-0n3j+j#wh$x2=$@u(we2itfi3h1k&(ff4ol#t+uwb_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    #'djangocms_admin_style',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sqlite3',
    'photos',
    'uploads',
    'lms',
    'location',
    'speaker',
    'reporting',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'piction.urls'

WSGI_APPLICATION = 'piction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'piction',
        'USER': 'roman',
        'PASSWORD': 'snickers',
        'HOST': '192.168.0.7'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


PROJECT_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(PROJECT_DIR, os.pardir)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(CONTENT_DIR, 'static'),)
STATIC_ROOT = 'staticfiles'

#Media

#MEDIA_URL = 'http://localhost:8000/media'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
#MEDIA_DIRS = os.path.join(CONTENT_DIR, 'media')
#MEDIAFILES_LOCATION = 'media'

TEMPLATES = '/templates'
TEMPLATE_DIRS = (os.path.join(CONTENT_DIR, 'templates'),)

LOGIN_REDIRECT_URL = 'authentication/'
LOGOUT_URL = '/templates/sign_up.html'

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        )

###Heroku settings - allowed_hosts and static stuff setup above
import dj_database_url
#DATABASES['default'] = dj_database_url.config()
#DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3',
#DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')

#Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
