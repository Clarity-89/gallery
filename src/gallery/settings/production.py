from .base import *

import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
#
# Standard Django settings.
#

DEBUG = False
ENVIRONMENT = 'production'

ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

DATABASES['default'].update(db_from_env)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'storages'
]

# Caching templates.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

# Production logging facility.
LOGGING['loggers'].update({
    '': {
        'handlers': ['sentry'],
        'level': 'ERROR',
        'propagate': False,
    },
    'gallery': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django.security.DisallowedHost': {
        'handlers': ['django'],
        'level': 'CRITICAL',
        'propagate': False,
    },
})

#
# Custom settings
#

# Show active environment in admin.
SHOW_ALERT = False

# We will assume we're running under https
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
# Only set this when we're behind Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING['handlers'].update({
    'sentry': {
        'level': 'WARNING',
        'class': 'raven.handlers.logging.SentryHandler',
    },
})

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# AWS Storage
AWS_STORAGE_BUCKET_NAME = 'gallery-viewer'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# E-Mail settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True