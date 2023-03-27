from configs.encryption import encrypt, decrypt
import secrets


# For SECRET_KEY generation
def generate_secret_key():
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = encrypt(''.join(secrets.choice(charset) for _ in range(50)))
    return SECRET_KEY


#########################
#                       #
#   Required settings   #
#                       #
#########################


# Uncomment to put the Project Name to change the default project name
PROJECT_NAME = 'Django Template'


# Set Environment
# ENV = 'dev'


# This is a list of valid fully-qualified domain names (FQDNs) for app/project.
#
# Example: ALLOWED_HOSTS = ['app.example.com', 'app.internal.local']
ALLOWED_HOSTS = []

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. NetBox will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY_GENERATED = False
SECRET_KEY = decrypt(generate_secret_key())

# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
DEBUG = False

# CELERY STUFF
#Install kombu (pip install kombu) and uncomment below if need to use celery
# from kombu import Queue

"""CELERY = {
    'CELERY_BROKER_URL': 'redis://localhost:6379/x',  # Change x to unused number
    'CELERY_RESULT_BACKEND': 'redis://localhost:6379/x',  # Change x to unused number
    'CELERY_ACCEPT_CONTENT': ['application/json'],
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json'
}"""

#change this ensure its unique name withith host or redis server
CELERY_DEFAULT_QUEUE = 'project_name_default'
CELERY_QUEUES = (
    # Queue('default'),
    # Queue('priority_high'),
)

CELERY_ROUTES = {
    # 'API.utils.ExecuteTask': {'queue': 'priority_high'},
    # 'scheduler.tasks.child': {'queue': 'priority_high'},
}

# URL PATH of the project. remove. Don't put '/' at the end of the URL.
URL_PATH = 'https://app.example.com'


# Database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases

"""DATABASE = {
	'ENGINE': '',
    'NAME': '',
    'USER': '',
    'PASSWORD': decrypt('encrypted password'),
    'HOST': '',
    'PORT': 6603,
	'CONN_HEALTH_CHECKS: True, # Check if the health check fails, the connection will be reestablished
    #'CONN_MAX_AGE': 300,      # Max database connection age in second
}"""

#########################
#                       #
#   Optional settings   #
#                       #
#########################

# Base URL path if accessing the app/project within a directory. For example, if installed at https://example.com/app/, set:
# BASE_PATH = 'app/'
BASE_PATH = ''

# API Cross-Origin Resource Sharing (CORS) settings. If CORS_ORIGIN_ALLOW_ALL is set to True, all origins will be
# allowed. Otherwise, define a list of allowed origins using either CORS_ORIGIN_WHITELIST or
# CORS_ORIGIN_REGEX_WHITELIST. For more information, see https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    # 'https://hostname.example.com',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    # r'^(https?://)?(\w+\.)?example\.com$',
]

CORS_EXPOSE_HEADERS = [
    # 'Content-Disposition',
    # 'Access-Control-Allow-Origin',
    # 'Access-Control-Request-Method',
    # 'Access-Control-Request-Headers',
    # 'X-API-KEY'
]

CORS_ALLOW_HEADERS = [
    # 'accept',
    # 'accept-encoding',
    # 'authorization',
    # 'content-type',
    # 'dnt',
    # 'origin',
    # 'user-agent',
    # 'x-csrftoken',
    # 'x-requested-with',
    # 'x-api-key',
]


# Automatically reset the lifetime of a valid session upon each authenticated request. Enables users to remain
# authenticated to NetBox indefinitely.
LOGIN_PERSISTENCE = False

# Setting this to True to close session when the user close the browser.
LOGIN_EXPIRED = False

# The length of time (in seconds) for which a user will remain logged into the web UI before being prompted to
# re-authenticate. (Default: 1209600 [14 days])
LOGIN_TIMEOUT = None

# Remote authentication support

#
# LDAP Configs
#

#install python-ldap and django-auth-ldap and uncomment below if will use LDAP
#from django_auth_ldap.config import LDAPGroupQuery

# Remote authentication support, comment out for LDAP authentication
# REMOTE_AUTH_BACKEND = 'configs.authentication.LDAPBackend'

# Define LDAP Address
LDAP_ADDRESS = 'ldaps://ldaps.domain.com:3269'


# To get User DN; run "dsquery user -samid USERNAME" in windows command prompt or powershell
LDAP_USER = ''  # LDAP User DN

# Enter encrypted password
LDAP_PASS = '' #decrypt('encrypted password')


# Define a group required to login.
# To get Group DN; run "dsquery group -samid GROUPNAME" in windows command prompt or powershell
# AUTH_LDAP_REQUIRE_GROUP = ''
AUTH_LDAP_REQUIRE_GROUP = 'Group DN'

# List the groups that will add and map to Django groups
# AUTH_LDAP_MIRROR_GROUPS = []
AUTH_LDAP_MIRROR_GROUPS = [
    #'Security Group Name',
]


# Define special user types using groups. Exercise great caution when assigning superuser status.
# To get Group DN; run "dsquery group -samid GROUPNAME" in windows command prompt or powershell
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    #'is_active': 'Group DN',
    #'is_staff': 'Group DN',
    #'is_superuser': 'Group DN',
    # Example of multiple group
    """'is_staff': (
        LDAPGroupQuery('Group DN') |
        LDAPGroupQuery('Group DN')
    )"""
}

#LDAP_ROOT_DN = "dc=abc,dc=domain,dc=com"

# The name to use for the csrf token cookie.
CSRF_COOKIE_NAME = 'csrftoken'

# Time zone (default: UTC)
TIME_ZONE = 'Asia/Singapore'

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date
DATE_FORMAT = 'Y-m-d'
SHORT_DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:M:S'
SHORT_TIME_FORMAT = 'H:M'
DATETIME_FORMAT = 'Y-m-d H:M:S'
SHORT_DATETIME_FORMAT = 'Y-m-d'


DEVICE_USER = ''
DEVICE_PASS = ''  #decrypt('encrypted pass')
DEVICE_ADMIN = ''
DEVICE_ADMIN_PASS = ''  #decrypt('encrypted pass')


# Enable custom logging. Please see the Django documentation for detailed guidance on configuring custom logs:
#   https://docs.djangoproject.com/en/stable/topics/logging/
"""LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django_auth_ldap': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}"""
