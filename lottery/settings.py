"""
Django settings for lottery project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rz5e5m#%y4xud0e^=z3ai=_l#^4c7tghfls06-@euhtt@27abj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lottery.apps.website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lottery.urls'

WSGI_APPLICATION = 'lottery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
MYSQL_PORT = '3307'
MYSQL_USER = 'yw14ylzoxy'
MYSQL_PASS = 'lj5yk053wmlm1hjikkjklh3wixwl2kz3044iw2zh'
MYSQL_DB   = 'app_pailie3'


# from sae._restful_mysql import monkey
# monkey.patch()
if False:
    DATABASES = {
        'default': {
                'ENGINE':   'django.db.backends.mysql',
                'NAME':     MYSQL_DB,
                'USER':     MYSQL_USER,
                'PASSWORD': MYSQL_PASS,
                'HOST':     MYSQL_HOST,
                'PORT':     MYSQL_PORT,
        }
    }

else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh/cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'


STATICFILES_DIRS = (
    location('static'),
)

TEMPLATE_DIRS = (
    location('templates'),
)
