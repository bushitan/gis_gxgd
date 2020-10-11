# -*- coding: utf-8 -*-

"""
Django settings for gis_gxgd project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'slg3bk5_2l8bk3bkxq%n3ewg3=+8trpn!i@3q-^rd+)*0r4xtq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lite',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'lite.middleware.session.SessionMiddleware',
)

ROOT_URLCONF = 'gis_gxgd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'gis_gxgd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False #计算机所在地时间#



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\','/')
 
STATICFILES_DIRS =(
  ("css", os.path.join(STATIC_ROOT,'css').replace('\\','/')),
  ("js", os.path.join(STATIC_ROOT,'js').replace('\\','/')),
)
 
STATIC_URL = '/static/'
 
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    #'DIRS':TEMPLATE_DIRS,
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.static',
      ],
    },
  },
]
# log配置
LOG_FILE = "./all.log"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
        },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(module)s : %(message)s'
            },
        'verbose': {
            'format':
                '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
            }
        },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
            },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
            },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_FILE,
            'mode': 'a',
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
            }
        },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
         'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
