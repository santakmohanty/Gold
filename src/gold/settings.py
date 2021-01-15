import os

# YAML configurations
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 'src' is BASE_DIR

# 'src/config/config.yml'
CONFIG_FILE = os.path.join(BASE_DIR, '../', 'config', 'config.yml')

# config_data will contain configuration details like credentials, API Keys, Secret Keys
with open(CONFIG_FILE) as f:
    config_data = yaml.safe_load(f)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_data['SECRET_KEY']
CONFIG = config_data

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config_data.get('DEBUG')

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = config_data.get('EMAIL_USE_TLS')
EMAIL_HOST = config_data.get('EMAIL_HOST')
EMAIL_PORT = config_data.get('EMAIL_PORT')
EMAIL_HOST_USER = config_data.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config_data.get('EMAIL_HOST_PASSWORD')

FROM_EMAIL = config_data.get('FROM_EMAIL')

if not DEBUG:
    # The recipient whom server will send the error report.
    # 'ADMINS' is for HTTP 5xx error-codes.
    # 'MANAGERS' for  HTTP 404 error-code.
    ADMINS = MANAGERS = [("BombaySoftwares", 'tech@bombaysoftwares.com'), ]
    # SERVER_EMAIL acts as server which sends the error reports to ADMINS and MANAGERS
    SERVER_EMAIL = FROM_EMAIL

HASHIDS_SALT = config_data.get('HASHIDS_SALT')
BASE_URL = config_data.get('BASE_URL')
LOG_FILE_PATH = config_data.get('LOG_FILE_PATH')
# Application definition


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.main',
]

# Cache backend is optional, but recommended to speed up user agent parsing
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
#
# # Name of cache backend to cache user agents. If it not specified default
# # cache alias will be used. Set to `None` to disable caching.
# USER_AGENTS_CACHE = 'default'


MIDDLEWARE = [

    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'apps.main.middleware.disable_csrf_middleware.DisableCSRFMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'apps.main.middleware.admin_auth_middleware.AdminAuthMiddleware',
]

ROOT_URLCONF = 'gold.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'apps', 'main', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'apps.main.jinja2.environment',
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
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

WSGI_APPLICATION = 'gold.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_data['POSTGRES_DB_CREDENTIALS']['DATABASE_NAME'],
        'USER': config_data['POSTGRES_DB_CREDENTIALS']['USERNAME'],
        'PASSWORD': config_data['POSTGRES_DB_CREDENTIALS']['PASSWORD'],
        'HOST': config_data['POSTGRES_DB_CREDENTIALS']['HOST'],
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-IN'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_BROWSER_XSS_FILTER = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'apps', 'main', 'static'),
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL of uploaded media files
MEDIA_URL = '/media/'

# Where media files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_PATH + 'app.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'apps': {
            'handlers': ['log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['console', 'mail_admins'],
        'level': 'DEBUG'
    },
}
