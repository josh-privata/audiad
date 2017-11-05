from os import environ, getenv
from os.path import abspath, dirname, join
from sys import argv
import logging
import logging.config
from elasticsearch import Elasticsearch
from configurations import Configuration
import os
import raven
from elasticsearch import RequestsHttpConnection

BASE_DIR = dirname(dirname(abspath(__file__)))
PROJECT_NAME = 'audiad'
PROJECT_ENVIRONMENT_SLUG = '{}_{}'.format(PROJECT_NAME, environ.get('DJANGO_CONFIGURATION'))

# Detect if we are running tests.  Is this really the best way?
IN_TESTS = 'test' in argv


class RedisCache(object):
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'KEY_PREFIX': 'audiad',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                # You may want this. See https://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
                # 'IGNORE_EXCEPTIONS': True, # see
            }
        }
    }
    CACHE_TTL = 60 * 15


class ElasticSearch(object):
    ES_CLIENT = Elasticsearch(
        ['http://127.0.0.1:9200/'], connection_class=RequestsHttpConnection)

    ELASTICSEARCH_DSL = {
        'default': {
            'hosts': 'localhost:9200'
        },
    }

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'audiad',
        },
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


class Common(Configuration):
    ADMINS = (
        ('Josh Cannons', 'josh.cannons@gmail.com'),
    )

    MANAGERS = ADMINS

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '21@coffee'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        'raven.contrib.django.raven_compat',
        'debug_toolbar',
        'bootstrap3',
        'django_extensions',
        'clear_cache',
        'django_tables2',
        'taggit',
        'django_filters',
        'elasticsearch_dsl',
        'widget_tweaks',
        'mptt',
        'music',

    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ROOT_URLCONF = 'audiad.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                join(BASE_DIR, 'templates')
            ],
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

    WSGI_APPLICATION = 'audiad.wsgi.application'


    # Password validation
    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'en-GB'

    TIME_ZONE = 'Australia/Brisbane'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = join(BASE_DIR, 'static_root')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # Additional locations of static files
    STATICFILES_DIRS = [
        join(BASE_DIR, 'static'),
        join(BASE_DIR, 'node_modules'),
    ]

    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # DATABASES = {
    #      'default': {
    #          'ENGINE': 'django.db.backends.postgresql',
    #          'NAME': 'django1',
    #          'USER': 'postgres',
    #          'PASSWORD': 'coffee',
    #          'HOST': '192.168.2.10',
    #          'PORT': '49162',
    #      }
    # }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }
    FIXTURE_DIRS = [
        join(BASE_DIR, 'fixtures')
    ]

    RAVEN_CONFIG = {
        'dsn': 'https://1c89626d8e02478e972af34e31360744:616e20a1933c4eb4ae3943c6b41dc3c7@sentry.io/240094',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            }
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }

    LOGOUT_REDIRECT_URL = '/'


class Dev(Common, RedisCache):
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/app-emails'
    INTERNAL_IPS = ['127.0.0.1', ]


class Deployed(RedisCache, Common):
    """
    Settings which are for a non local deployment, served behind nginx.
    """
    # django-debug-toolbar will throw an ImproperlyConfigured exception if DEBUG is
    # ever turned on when run with a WSGI server
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    PUBLIC_ROOT = join(BASE_DIR, '../public/')
    STATIC_ROOT = join(PUBLIC_ROOT, 'static')
    MEDIA_ROOT = join(PUBLIC_ROOT, 'media')
    COMPRESS_OUTPUT_DIR = ''

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'josh.cannons#gmail.com'
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''
    SERVER_EMAIL = ''


class Stage(Deployed):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getenv('POSTGRES_USER', ''),
            'USER': getenv('POSTGRES_USER', ''),
            'PASSWORD': getenv('POSTGRES_PASSWORD', 'password'),
            'HOST': getenv('POSTGRES_SERVICE_HOST', 'localhost'),
        }
    }


class Prod(Deployed):
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getenv('POSTGRES_USER', ''),
            'USER': getenv('POSTGRES_USER', ''),
            'PASSWORD': getenv('POSTGRES_PASSWORD', 'password'),
            'HOST': getenv('POSTGRES_SERVICE_HOST', 'localhost'),
        }
    }

    ALLOWED_HOSTS = ['.audiad.com', ]  # add deployment domain here

    RAVEN_CONFIG = {
        'dsn': ''
    }
