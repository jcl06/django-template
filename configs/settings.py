"""
Django settings for configs project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


import importlib
import os
import platform
import sys
from django.core.exceptions import ImproperlyConfigured
from .generate_secret_key import generate_secret_key
#
# Environment setup
#

VERSION = '2.0'

# Hostname
HOSTNAME = platform.node()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Validate Python version
if sys.version_info < (3, 8):
    raise RuntimeError(
        f"This application requires Python 3.8 or later. (Currently installed: Python {platform.python_version()})"
    )

#
# Import Project Configuration
#

# Import configuration parameters

config_path = os.getenv('configuration', 'configs.configuration')
try:
    configuration = importlib.import_module(config_path)
except ModuleNotFoundError as e:
    if getattr(e, 'name') == config_path:
        raise ImproperlyConfigured(
            f"Specified configuration module ({config_path}) not found. Please define project_name/configs/configuration.py"
        )
    raise

# Enforce required configuration parameters
for parameter in ['ALLOWED_HOSTS', 'SECRET_KEY', 'URL_PATH', 'SECRET_KEY_GENERATED']:
    if not hasattr(configuration, parameter):
        raise ImproperlyConfigured(f"Required parameter {parameter} is missing from configuration.")
    else:
        if isinstance(getattr(configuration, parameter), bool):
            continue
        if not getattr(configuration, parameter):
            raise ImproperlyConfigured(f"{parameter} is empty.")

# Set required parameters
SECRET_KEY_GENERATED = getattr(configuration, 'SECRET_KEY_GENERATED')
if not SECRET_KEY_GENERATED:
    generate_secret_key()
ALLOWED_HOSTS = getattr(configuration, 'ALLOWED_HOSTS')
CLRY = getattr(configuration, 'CELERY', {})
SECRET_KEY = getattr(configuration, 'SECRET_KEY')
URL_PATH = getattr(configuration, 'URL_PATH')



# Set static config parameters
BASE_PATH = getattr(configuration, 'BASE_PATH', '')
if BASE_PATH:
    BASE_PATH = BASE_PATH.strip('/') + '/'  # Enforce trailing slash only

PROJECT_NAME = getattr(configuration, 'PROJECT_NAME', 'Django Template')
DATABASE = getattr(configuration, 'DATABASE', {'ENGINE': 'django.db.backends.sqlite3', 'NAME': f'{BASE_DIR}/db.sqlite3',})

REMOTE_AUTH_BACKEND = getattr(configuration, 'REMOTE_AUTH_BACKEND', None)
if REMOTE_AUTH_BACKEND:
    LDAP_ENABLED = True
    # Enforce required LDAP configuration parameters
    for parameter in ['LDAP_ADDRESS', 'LDAP_USER', 'LDAP_PASS', 'LDAP_ROOT_DN', 'AUTH_LDAP_REQUIRE_GROUP']:
        if not hasattr(configuration, parameter):
            raise ImproperlyConfigured(f"Required parameter {parameter} is missing from configuration.")
        else:
            if isinstance(getattr(configuration, parameter), bool):
                continue
            if not getattr(configuration, parameter):
                raise ImproperlyConfigured(f"{parameter} is empty.")
else:
    LDAP_ENABLED = False

LDAP_ADDRESS = getattr(configuration, 'LDAP_ADDRESS', '')
LDAP_USER = getattr(configuration, 'LDAP_USER', '')
LDAP_PASS = getattr(configuration, 'LDAP_PASS', '')
LDAP_ROOT_DN = getattr(configuration, 'LDAP_ROOT_DN', '')
AUTH_LDAP_REQUIRE_GROUP = getattr(configuration, 'AUTH_LDAP_REQUIRE_GROUP', '')
AUTH_LDAP_MIRROR_GROUPS = getattr(configuration, 'AUTH_LDAP_MIRROR_GROUPS', [])
AUTH_LDAP_USER_FLAGS_BY_GROUP = getattr(configuration, 'AUTH_LDAP_USER_FLAGS_BY_GROUP', {})

CORS_ORIGIN_ALLOW_ALL = getattr(configuration, 'CORS_ORIGIN_ALLOW_ALL', False)
CORS_ORIGIN_REGEX_WHITELIST = getattr(configuration, 'CORS_ORIGIN_REGEX_WHITELIST', [])
CORS_ORIGIN_WHITELIST = getattr(configuration, 'CORS_ORIGIN_WHITELIST', [])
CORS_EXPOSE_HEADERS = getattr(configuration, 'CORS_EXPOSE_HEADERS', [])
CORS_ALLOW_HEADERS = getattr(configuration, 'CORS_ALLOW_HEADERS', [])

CSRF_COOKIE_NAME = getattr(configuration, 'CSRF_COOKIE_NAME', 'csrftoken')
CSRF_TRUSTED_ORIGINS = getattr(configuration, 'CSRF_TRUSTED_ORIGINS', [URL_PATH])
LOGIN_PERSISTENCE = getattr(configuration, 'LOGIN_PERSISTENCE', False)
LOGIN_EXPIRED = getattr(configuration, 'LOGIN_EXPIRED', False)
LOGIN_TIMEOUT = getattr(configuration, 'LOGIN_TIMEOUT', None)

DATE_FORMAT = getattr(configuration, 'DATE_FORMAT', 'Y-m-d')
DATETIME_FORMAT = getattr(configuration, 'DATETIME_FORMAT', 'Y-m-d H:M:S')
SHORT_DATE_FORMAT = getattr(configuration, 'SHORT_DATE_FORMAT', 'Y-m-d')
SHORT_DATETIME_FORMAT = getattr(configuration, 'SHORT_DATETIME_FORMAT', 'Y-m-d H:M:S')
SHORT_TIME_FORMAT = getattr(configuration, 'SHORT_TIME_FORMAT', 'H:M')
TIME_FORMAT = getattr(configuration, 'TIME_FORMAT', 'H:M')
TIME_ZONE = getattr(configuration, 'TIME_ZONE', 'UTC')

DEBUG = getattr(configuration, 'DEBUG', False)
LOGGING = getattr(configuration, 'LOGGING', {})

LOG_DIR = getattr(configuration, 'LOG_DIR', BASE_DIR)
if LOG_DIR:
    if not os.path.exists(LOG_DIR):
        # if the demo_folder directory is not present
        # then create it.
        os.makedirs(LOG_DIR)

CELERY_DEFAULT_QUEUE = getattr(configuration, 'CELERY_DEFAULT_QUEUE', '{0}_default'.format(PROJECT_NAME))
CLRY_QUEUES = getattr(configuration, 'CELERY_QUEUES', ())
CLRY_ROUTES = getattr(configuration, 'CELERY_ROUTES', ())

SUPPORT_EMAIL = getattr(configuration, 'SUPPORT_EMAIL', '')
EMAIL_API_URL = getattr(configuration, 'EMAIL_API_URL', '')

DEVICE_USER = getattr(configuration, 'DEVICE_USER', '')
DEVICE_PASS = getattr(configuration, 'DEVICE_PASS', '')
DEVICE_ADMIN = getattr(configuration, 'DEVICE_ADMIN', '')
DEVICE_ADMIN_PASS = getattr(configuration, 'DEVICE_ADMIN_PASS', '')

#
# Database
#

DATABASES = {
    'default': DATABASE,
}

# to disable the check
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

#
# Celery
#

if CLRY:
    BROKER_URL = CLRY['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = CLRY['CELERY_RESULT_BACKEND']
    CELERY_ACCEPT_CONTENT = CLRY['CELERY_ACCEPT_CONTENT']
    CELERY_TASK_SERIALIZER = CLRY['CELERY_TASK_SERIALIZER']
    CELERY_RESULT_SERIALIZER = CLRY['CELERY_RESULT_SERIALIZER']
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
    if CLRY_QUEUES:
        CELERY_QUEUES = CLRY_QUEUES
    if CLRY_ROUTES:
        CELERY_ROUTES = CLRY_ROUTES


#
# Sessions
#

if LOGIN_TIMEOUT:
    # Django default is 1209600 seconds (14 days)
    SESSION_COOKIE_AGE = LOGIN_TIMEOUT
SESSION_EXPIRE_AT_BROWSER_CLOSE = LOGIN_EXPIRED
SESSION_SAVE_EVERY_REQUEST = LOGIN_PERSISTENCE

#
# Django
#

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party apps
    #uncomment below if will use mobile UI
    #'django_user_agents',  # for app with mobile UI
    'import_export',
    'django_celery_beat', # scheduler
    # local apps
    'core',
    'scheduler',



]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #uncomment below if will use mobile UI
    #'django_user_agents.middleware.UserAgentMiddleware',  # Required by django_user_agents

]

USER_AGENTS_CACHE = 'default'  # Required by django_user_agents

ROOT_URLCONF = 'configs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI
WSGI_APPLICATION = 'configs.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'core.User'

if REMOTE_AUTH_BACKEND:
    AUTHENTICATION_BACKENDS = (
        REMOTE_AUTH_BACKEND,
        'django.contrib.auth.backends.ModelBackend',
    )

# Internationalization
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = f'/{BASE_PATH}static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Authentication URLs
LOGIN_URL = '/{}login/'.format(BASE_PATH)
LOGIN_REDIRECT_URL = f'/{BASE_PATH}'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
