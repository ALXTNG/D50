"""
Django settings for D50 project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
#~ from django.contrib.sites.models import Site

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1)oium_=!#qr0^g^)o#_h9y%t6pn&zzv6g%yan_er__i=308%z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'home',
    'workinprogress',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.admin',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'D50.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'D50.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#~ current_site = Site.objects.get_current()
#~ current_site.domain


LOGIN_REDIRECT_URL = '../'
#~ LOGIN_REDIRECT_URL = current_site.domain


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

ENV_PATH = os.path.abspath(os.path.dirname(__file__))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ENV_PATH, '../../D50/static/') 
MEDIA_ROOT = os.path.join(ENV_PATH, '../../D50/media/') 

#~ STATICFILES_DIRS = (
  #~ os.path.join(ENV_PATH, 'static/'),
#~ )

#~ EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#~ EMAIL_HOST = 'mail.gandi.net'
#~ EMAIL_HOST = 'smtp.gmail.com'
#~ EMAIL_PORT = 465
#~ EMAIL_HOST_USER = 'alessandro.tengattini@gmail.com'
#~ EMAIL_HOST_PASSWORD = 'I thought I needed a safer password'
#~ EMAIL_USE_TLS = True
#~ send_mail('test email', 'hello world', 'alessandro.tengattini@gmail.com', ['alessandro.tengattini@gmail.com','alextenga86@hotmail.it'])

#~ send_mail('test email', 'hello world', 'contact@next-grenoble.fr', ['alessandro.tengattini@gmail.com','alextenga86@hotmail.it'])

#~ DEFAULT_FROM_EMAIL = 'alessandro.tengattini@gmail.com'
#~ SERVER_EMAIL = 'alessandro.tengattini@gmail.com'
#~ EMAIL_USE_TLS = True
#~ EMAIL_HOST = 'smtp.gmail.com'
#~ EMAIL_PORT = 587
#~ EMAIL_HOST_USER = 'alessandro.tengattini@gmail.com'
#~ EMAIL_HOST_PASSWORD = 'I thought I needed a safer password'

DEFAULT_FROM_EMAIL = 'contact@next-grenoble.fr'
SERVER_EMAIL = 'contact@next-grenoble.fr'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.gandi.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact@next-grenoble.fr'
EMAIL_HOST_PASSWORD = 'pastascotta'
