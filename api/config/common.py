import os
from os.path import join

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'corsheaders',
        'rest_framework',  # utilities for rest apis
        # 'drf_yasg',
        # 'django_filters',  # for filtering rest endpoints
        # 'constance',  # Django Admin Dynamic Settings
        # 'constance.backends.database',
        # 'django_extensions',

        # Med app apps
        'api.users',
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
    
        # Important for Heroku and static files with wsgi
        'whitenoise.middleware.WhiteNoiseMiddleware',
        
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
        #CORS headers
        'corsheaders.middleware.CorsMiddleware',
    )
    
    # Only used for django admin
    # AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )

    # AUTH_USER_MODEL = 'core.User'

    # https://django-constance.readthedocs.io/en/latest/
    # CONSTANCE_CONFIG = {
    #     'TITLE': ('Med App Settings', 'Placeholder settings'),
    # }
    # CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
    
    ROOT_URLCONF = 'api.urls'

    WSGI_APPLICATION = 'api.wsgi.application'
    ALLOWED_HOSTS = ["*"]
    SECRET_KEY = values.SecretValue()

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    BASE_DIR = BASE_DIR
    STATICFILES_DIRS = []
    
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
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

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False, environ_name='DEBUG')

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Logging
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
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Django Rest Framework
    REST_FRAMEWORK = {
        # 'DEFAULT_PAGINATION_CLASS':
        # 'api.core.pagination.Pagination',
        # 'PAGE_SIZE':
        # int(os.getenv('DJANGO_PAGINATION_LIMIT', 1000000)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        # 'DEFAULT_PERMISSION_CLASSES': [
        #     'rest_framework.permissions.IsAuthenticated',
        # ],
        # 'DEFAULT_AUTHENTICATION_CLASSES': [
        #     'api.core.auth_backend.RealityCaptureAPIGWBackend',
        # ],
        # 'DEFAULT_FILTER_BACKENDS':
        # ['django_filters.rest_framework.DjangoFilterBackend'],
        # 'TEST_REQUEST_DEFAULT_FORMAT':
        # 'json',
        # 'EXCEPTION_HANDLER':
        # 'api.core.utils.exception_handler.custom_exception_handler'
    }
    
    # SWAGGER SETTINGS
    # TODO Add the Oauth configuration for hilti oauth
    # Now you can use an already existing token as the apiKey in swagger authorize
    # SWAGGER_SETTINGS = {
    #     'SECURITY_DEFINITIONS': {
    #         'Bearer': {
    #             'in': 'header',
    #             'name': 'Authorization',
    #             'type': 'apiKey',
    #         },
    #         "Hilti OAuth2": {
    #             "type": "oauth2",
    #             "authorizationUrl": "http://swagger.io/api/oauth/dialog",
    #             "flow": "implicit",
    #             "scopes": {
    #                 'write': 'Write everything',
    #             },
    #         }
    #     },
    # }

    # Cache config
    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #         'LOCATION': 'pm-cache',
    #     }
    # }

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    AUTH_USER_MODEL = 'users.User'
    # To allow all the ports accesss
    CORS_ORIGIN_ALLOW_ALL = True
    # For front end to able to get the cookies
    CORS_ALLOW_CREDENTIALS = True


    
    # for Heroku
    import django_on_heroku
    django_on_heroku.settings(locals(), staticfiles=False)