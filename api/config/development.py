import os

from .common import BASE_DIR, Common


class Development(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn", )

    # STATIC_ROOT = os.path.join(BASE_DIR, 'data', 'static')
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'data', 'media')

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    # Postgres  DB Settings
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': os.getenv('DATABASE_NAME'),
    #         'USER': os.getenv('DATABASE_USER'),
    #         'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    #         'HOST': os.getenv('DATABASE_HOST'),
    #         'PORT': os.getenv('DATABASE_PORT'),
    #     }
    # }
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgresql-aerodynamic-21838',
        }
    }
    
    DEBUG = True
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
                'handlers': ['console', 'django.server'],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }

