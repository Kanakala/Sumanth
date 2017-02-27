"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm1zb^(00z&nhg7pslvit(4135f^6k43d_gogr8&%oni^p2)p+5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Customer',
    'Restaurant',
    'custom_user',
    'rest_framework',
    'localflavor',
    'django_twilio',
    'django_nose',
    'crispy_forms',
	'widget_tweaks',
	'materializecssform',

]

AUTH_USER_MODEL = 'custom_user.EmailUser'

#PHONENUMBER_DB_FORMAT = 'NATIONAL'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_jsonp.renderers.JSONPRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}



MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'spicywagon',
		##'HOST': '/opt/bitnami/mysql/tmp/mysql.sock',
        # 'USER': 'root',
        # 'PASSWORD': 'sumanth',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    # }
# }

# DATABASES = {
	# 'default': {
		# 'ENGINE': 'django.db.backends.postgresql_psycopg2',
		# 'NAME': 'rail',
		# 'HOST': '/opt/bitnami/postgresql',
		# 'PORT': '5432',
		# 'USER': 'postgres',
		# 'PASSWORD': 'ZGGhJW8N1C42',
		# }
	# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		#'/opt/bitnami/apps/django/django_projects/Project/db.sqlite3',
		
    }
}




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

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'India+91'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'C:/Users/Sumanth/Desktop/railindia/mysite/Restaurant/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'C:/Users/Sumanth/Desktop/railindia/mysite/Restaurant/media'

TWILIO_ACCOUNT_SID = 'AC4d7afd5857aa5b7a784611ebb7a6f5bb'
TWILIO_AUTH_TOKEN = 'dce0a9273bd34dd8d5016c601460841c'

# The default callerid will be used for all outgoing phone calls and SMS
# messages if not explicitly specified. This number must be previously
# validated with twilio in order to work. See
# https://www.twilio.com/user/account/phone-numbers#
TWILIO_DEFAULT_CALLERID = ''