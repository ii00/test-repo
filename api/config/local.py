import os

import dj_database_url
from configurations import values

from .common import BASE_DIR, Common

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'


class Local(Common):
    # Read env variables from .env file if defined
    DOTENV_PATH = os.path.join(os.path.dirname(BASE_DIR), '.env')
    if os.path.isfile(DOTENV_PATH):
        DOTENV = DOTENV_PATH

    DEBUG = True

    INSTALLED_APPS = Common.INSTALLED_APPS

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(asctime)s] %(message)s',
            },
            'verbose': {
                'format':
                '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            }
        }
    }
    # Postgres settings
    
    
    DATABASE_URL = values.Value('postgres://postgres:postgrespw@localhost:55001',
                                environ_name='DATABASE_URL',
                                environ_prefix=None)
    
    POSTGRES_CONN_MAX_AGE = values.PositiveIntegerValue(
        600, environ_name='POSTGRES_CONN_MAX_AGE')
    
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('DATABASE_HOST'),
            'PORT': os.getenv('DATABASE_PORT'),
        }
    }    
    
